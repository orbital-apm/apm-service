-- Create the 'user' table
CREATE TABLE public."users" (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    username TEXT UNIQUE,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);

INSERT INTO public."users" (username, email, password)
VALUES ('admin', 'admin@admin.com', '$2b$12$TmUxhM.CLQwTttSwQ//pLe9D5YeHgiJKRXHAlTa0Ze0TcKn9tBMRy')

