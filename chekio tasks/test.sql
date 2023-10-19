
CREATE TABLE IF NOT EXISTS `building` (
    -- Primary key
    `id` INTEGER NOT NULL,

    -- Building address
    `address` TEXT NOT NULL,

    PRIMARY KEY(`id`)
);

CREATE TABLE IF NOT EXISTS `lector` (
    -- Primary key
    `id` INTEGER NOT NULL,

    -- First and last name of the lector
    `name` TEXT NOT NULL,

    -- Lector's age
    `age` INTEGER NOT NULL,

    -- Lector's sex
    `sex` INTEGER NOT NULL,

    -- Unique string identifier
    `keycard` TEXT NOT NULL,

    PRIMARY KEY(`id`)
);

CREATE UNIQUE INDEX IF NOT EXISTS `idx_lector_keycard` ON `lector`(`keycard`);

CREATE TABLE IF NOT EXISTS `dorm` (
    -- Reference to building
    `building_id` INTEGER NOT NULL,

    -- Name of the manager
    `manager` TEXT NOT NULL,

    PRIMARY KEY(`building_id`),

    FOREIGN KEY(`building_id`) REFERENCES `building`(`id`)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS `cathedra` (
    -- Primary key
    `id` INTEGER NOT NULL,

    -- Name of the cathedra
    `name` TEXT NOT NULL,

    -- Reference to lector
    `head_id` INTEGER NOT NULL,

    -- Reference to building
    `headoffice_id` INTEGER NOT NULL,

    PRIMARY KEY(`id`),

    FOREIGN KEY(`head_id`) REFERENCES `lector`(`id`)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    FOREIGN KEY(`headoffice_id`) REFERENCES `building`(`id`)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);

CREATE UNIQUE INDEX  IF NOT EXISTS `idx_cathedra_head_id` ON `cathedra`(`head_id`);

CREATE INDEX IF NOT EXISTS `idx_cathedra_headoffice_id` ON `cathedra`(`headoffice_id`);

CREATE TABLE IF NOT EXISTS `cathedra_lector` (
    -- Reference to cathedra
    `cathedra_id` INTEGER NOT NULL,

    -- Reference to lector
    `lector_id` INTEGER NOT NULL,

    PRIMARY KEY(`cathedra_id`, `lector_id`),

    FOREIGN KEY(`cathedra_id`) REFERENCES `cathedra`(`id`)
        ON UPDATE CASCADE
        ON DELETE CASCADE,

    FOREIGN KEY(`lector_id`) REFERENCES `lector`(`id`)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

CREATE INDEX IF NOT EXISTS `idx_cathedra_lector_lector_id` ON `cathedra_lector`(`lector_id`);

CREATE TABLE IF NOT EXISTS `student` (
    -- Primary key
    `id` INTEGER NOT NULL,

    -- First and last name of the student
    `name` TEXT NOT NULL,

    -- Reference to cathedra
    `cathedra_id` INTEGER NOT NULL,

    -- Reference to dorm
    `dorm_id` INTEGER NULL,

    PRIMARY KEY(`id`),

    FOREIGN KEY(`cathedra_id`) REFERENCES `cathedra`(`id`)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    FOREIGN KEY(`dorm_id`) REFERENCES `dorm`(`building_id`)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);

CREATE INDEX IF NOT EXISTS `ìdx_student_cathedra_id` ON `student`(`cathedra_id`);