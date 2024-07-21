-- Create the 'users' table
CREATE TABLE public."users" (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    username TEXT UNIQUE,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);

-- Create the 'keycaps' table
CREATE TABLE public."keycaps" (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name TEXT NOT NULL,
    price NUMERIC(10, 2),
    manufacturer TEXT,
    vendor VARCHAR[],
    colors VARCHAR[],
    layout VARCHAR[],
    material TEXT,
    profile VARCHAR[],
    img_url TEXT,
    availability BOOLEAN
);

-- Create the 'switches' table
CREATE TABLE public."switches" (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name TEXT NOT NULL,
    price NUMERIC(10, 2),
    manufacturer TEXT,
    switch_type TEXT,
    actuation_force NUMERIC(10, 2),
    travel_distance NUMERIC(10, 2),
    vendor VARCHAR[],
    img_url TEXT,
    availability BOOLEAN
);

-- Create the 'kits' table
CREATE TABLE public."kits" (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name TEXT NOT NULL,
    price NUMERIC(10, 2),
    manufacturer TEXT,
    vendor VARCHAR[],
    layout_size VARCHAR[],
    layout_standard VARCHAR[],
    layout_ergonomic TEXT,
    hotswappable BOOLEAN,
    knob_support BOOLEAN,
    rgb_support BOOLEAN,
    display_support BOOLEAN,
    connection VARCHAR[],
    mount_style TEXT,
    material TEXT,
    img_url TEXT,
    availability BOOLEAN
);

-- Create the 'lubricants' table

CREATE TABLE public."lubricants" (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR NOT NULL,
    price NUMERIC(10, 2),
    img_url TEXT,
    availability BOOLEAN
);

-- Create the 'builds' table

CREATE TABLE public."builds" (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    build_name TEXT,
    kit_choice TEXT,
    switch_choice TEXT,
    keycap_choice TEXT,
    lubricant_choice TEXT,
);





