import { test, expect } from '@playwright/test';

test('homepage loads with correct title', async ({ page }) => {
    await page.goto('/');

    // Check page title
    await expect(page).toHaveTitle(/Don't Compete/);

    // Check hero heading
    await expect(page.getByRole('heading', { name: /Master Your Exams/i })).toBeVisible();

    // Check site description
    await expect(page.getByText(/free, community-driven learning platform/i)).toBeVisible();
});

test('homepage shows exam selection section', async ({ page }) => {
    await page.goto('/');

    // Check "Select Your Exam" heading
    await expect(page.getByRole('heading', { name: /Select Your Exam/i })).toBeVisible();

    // Either loading spinner or exam cards or "no exams" message should be visible
    const hasSpinner = await page.locator('.loading-spinner').isVisible().catch(() => false);
    const hasExams = await page.locator('.card').count() > 0;
    const hasNoExamsMessage = await page.getByText(/No exams found/i).isVisible().catch(() => false);

    expect(hasSpinner || hasExams || hasNoExamsMessage).toBeTruthy();
});

test('homepage shows feature cards', async ({ page }) => {
    await page.goto('/');

    // Check for feature cards
    await expect(page.getByRole('heading', { name: /Comprehensive Theory/i })).toBeVisible();
    await expect(page.getByRole('heading', { name: /PYQ Practice/i })).toBeVisible();
    await expect(page.getByRole('heading', { name: /Smart Learning/i })).toBeVisible();
});

test('footer displays correctly', async ({ page }) => {
    await page.goto('/');

    // Check footer content
    await expect(page.getByText(/Apache 2.0 License/i)).toBeVisible();
    await expect(page.getByRole('link', { name: /Apache 2.0 License/i })).toHaveAttribute('href', 'https://github.com/imxade/dontcompete');
});

test.skip('theme toggle works', async ({ page }) => {
    await page.goto('/');

    // Get initial theme
    const html = page.locator('html');
    const initialTheme = await html.getAttribute('data-theme');

    // Theme should be either dracula, cupcake, or null
    expect(initialTheme === null || ['dracula', 'cupcake'].includes(initialTheme)).toBeTruthy();

    // Click theme toggle button
    await page.getByRole('button', { name: /Toggle theme/i }).click();

    // Wait a bit for theme to change
    await page.waitForTimeout(100);

    // Theme should have changed
    const newTheme = await html.getAttribute('data-theme');
    expect(newTheme).not.toBe(initialTheme);
    expect(newTheme === null || ['dracula', 'cupcake'].includes(newTheme)).toBeTruthy();
});

test('navigation header is present', async ({ page }) => {
    await page.goto('/');

    // Check for site name in header
    await expect(page.getByRole('link', { name: /Don't Compete/i }).first()).toBeVisible();

    // Check theme toggle button exists
    await expect(page.getByRole('button', { name: /Toggle theme/i })).toBeVisible();
});
