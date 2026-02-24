-- Normalized Schema for Knowledge Base

CREATE TABLE IF NOT EXISTS streams (
    code VARCHAR,
    name VARCHAR,
    PRIMARY KEY (code)
);

CREATE TABLE IF NOT EXISTS subjects (
    id VARCHAR,
    stream_code VARCHAR,
    name VARCHAR,
    order_index INTEGER,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS subtopics (
    id VARCHAR,
    subject_id VARCHAR,
    name VARCHAR,
    description TEXT,
    order_index INTEGER,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS questions (
    id VARCHAR, -- Composite Global ID e.g. "cs_2024-M_1"
    stream_code VARCHAR,
    packet_id VARCHAR,
    question_no VARCHAR,
    q_type VARCHAR,
    q_key VARCHAR,
    q_text TEXT,
    a_text TEXT,
    exp_text TEXT,
    subtopic_id VARCHAR, -- Nullable initially
    img_path_q VARCHAR,
    img_path_exp VARCHAR,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS theory (
    id VARCHAR,
    subtopic_id VARCHAR,
    content_md TEXT, -- generated theory content
    PRIMARY KEY (id)
);
