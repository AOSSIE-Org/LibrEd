"""
Image optimization utilities for asset generation.

This module provides functions to optimize images for web delivery,
supporting both PNG optimization and WebP conversion with configurable
quality settings.
"""

import logging
from PIL import Image
from typing import Literal, Optional
from pathlib import Path

logger = logging.getLogger(__name__)

ImageFormat = Literal["png", "webp"]


def optimize_image(
    image: Image.Image,
    output_path: str,
    format: ImageFormat = "webp",
    quality: int = 85,
    lossless: bool = False,
) -> None:
    """
    Optimize and save an image with specified format and quality settings.
    
    Args:
        image: PIL Image object to optimize
        output_path: Path where the optimized image will be saved
        format: Output format - 'png' or 'webp' (default: 'webp')
        quality: Quality level 1-100 for lossy compression (default: 85)
                 Higher values = better quality but larger files
        lossless: Use lossless compression (default: False)
                  For WebP: True = lossless, False = lossy
                  For PNG: This parameter is ignored (PNG is always lossless)
    
    Returns:
        None
    
    Example:
        >>> img = Image.open("source.png")
        >>> optimize_image(img, "output.webp", format="webp", quality=85)
        >>> optimize_image(img, "output.png", format="png")
    """
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    if format == "webp":
        _save_as_webp(image, output_path, quality, lossless)
    elif format == "png":
        _save_as_png(image, output_path)
    else:
        raise ValueError(f"Unsupported format: {format}. Use 'png' or 'webp'.")
    
    logger.debug(f"Saved optimized {format.upper()} to {output_path}")


def _save_as_webp(
    image: Image.Image,
    output_path: Path,
    quality: int,
    lossless: bool
) -> None:
    """Save image as WebP with specified quality settings."""
    save_kwargs = {
        "format": "WebP",
        "lossless": lossless,
    }
    
    if not lossless:
        save_kwargs["quality"] = quality
        save_kwargs["method"] = 6  # 0-6, higher = slower but better compression
    
    image.save(output_path, **save_kwargs)


def _save_as_png(image: Image.Image, output_path: Path) -> None:
    """Save image as optimized PNG."""
    image.save(
        output_path,
        format="PNG",
        optimize=True,
        compress_level=9  # Maximum compression (0-9)
    )


def get_file_extension(format: ImageFormat) -> str:
    """
    Get the file extension for a given image format.
    
    Args:
        format: Image format ('png' or 'webp')
    
    Returns:
        File extension with dot (e.g., '.webp')
    """
    return f".{format}"


def convert_existing_image(
    input_path: str,
    output_path: Optional[str] = None,
    format: ImageFormat = "webp",
    quality: int = 85,
    lossless: bool = False,
) -> str:
    """
    Convert an existing image file to optimized format.
    
    Args:
        input_path: Path to source image
        output_path: Path for output (if None, replaces extension of input_path)
        format: Target format - 'png' or 'webp'
        quality: Quality level for lossy compression (1-100)
        lossless: Use lossless compression
    
    Returns:
        Path to the converted image
    
    Example:
        >>> convert_existing_image("image.png", format="webp", quality=85)
        'image.webp'
    """
    input_path = Path(input_path)
    
    if output_path is None:
        output_path = input_path.with_suffix(get_file_extension(format))
    else:
        output_path = Path(output_path)
    
    with Image.open(input_path) as img:
        # Convert RGBA to RGB if saving as format that doesn't support transparency
        if img.mode == "RGBA" and format not in ["png", "webp"]:
            # Create white background
            background = Image.new("RGB", img.size, (255, 255, 255))
            background.paste(img, mask=img.split()[3])  # Use alpha channel as mask
            img = background
        
        optimize_image(img, str(output_path), format, quality, lossless)
    
    return str(output_path)
