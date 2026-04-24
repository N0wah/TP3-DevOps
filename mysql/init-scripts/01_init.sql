-- ============================================================
--  Initialisation MySQL — table utilisateurs (4 entrées requises)
-- ============================================================

CREATE TABLE IF NOT EXISTS utilisateurs (
    id         INT            AUTO_INCREMENT PRIMARY KEY,
    nom        VARCHAR(100)   NOT NULL,
    email      VARCHAR(255)   NOT NULL UNIQUE,
    role       VARCHAR(50)    NOT NULL,
    created_at TIMESTAMP      NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

INSERT INTO utilisateurs (nom, email, role) VALUES
    ('Alice Martin',    'alice@example.com',   'admin'),
    ('Bob Dupont',      'bob@example.com',     'user'),
    ('Charlie Bernard', 'charlie@example.com', 'user'),
    ('Diana Lemaire',   'diana@example.com',   'moderator');
