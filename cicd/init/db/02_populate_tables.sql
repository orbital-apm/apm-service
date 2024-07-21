-- Populate the 'users' table
INSERT INTO public."users" (username, email, password) VALUES
('user1', 'user1@example.com', 'hashed_password_1'),
('user2', 'user2@example.com', 'hashed_password_2'),
('user3', 'user3@example.com', 'hashed_password_3');

-- Populate the 'keycaps' table
INSERT INTO public."keycaps" (name, price, manufacturer, vendor, colors, layout, material, profile, img_url, availability) VALUES
('Skyloong Neon', 39.0, 'Skyloong', ARRAY["Epomaker"], ARRAY[], ARRAY["ANSI"], 'PBT', ARRAY['Cherry'], 'https://example.com/skyloong-neon.jpg', true),
('Diykeycap Red Samurai', 42.0, 'Diykeycap', ARRAY["Diykeycap"], ARRAY[], ARRAY["ISO","ANSI"], 'ABS', ARRAY['NSA'], 'https://example.com/diykeycap-red-samurai.jpg', true),
("Keyreative Cat's Eye", 31.0, 'Keyreative', ARRAY["zFrontier"], ARRAY[], ARRAY["ISO"], 'PC', ARRAY['Cherry'], 'https://example.com/keyreative-cat-eye.jpg', false);

-- Populate the 'switches' table
INSERT INTO public."switches" (name, price, manufacturer, switch_type, actuation_force, travel_distance, vendor, img_url, availability) VALUES
('Ktt Strawberry', 0.29, 'Ktt', 'Linear', 62.0, 4.0, ARRAY["MK"], 'https://example.com/ktt-strawberry.jpg', true),
('Epomaker Comte Semisilent', 0.72, 'Epomaker', 'Silent Linear', 67.0, 3.8, ARRAY['Amazon'], 'https://example.com/epomaker-comte-semisilent.jpg', true),
('Kailh BOX Jade Clicky', 0.51, 'Kailh', 'Clicky', 50.0, 3.6, ARRAY['Dangkeebs'], 'https://example.com/kailh-box-jade-clicky.jpg', false);

-- Populate the 'kits' table
INSERT INTO public."kits" (name, price, manufacturer, vendor, layout_size, layout_standard, layout_ergonomic, hotswappable, knob_support, rgb_support, display_support, connection, mount_style, material, img_url, availability) VALUES
('Tofu65', 185.00, 'KBDfans', ARRAY['KBDfans'], ARRAY['65%'], ARRAY['ANSI'],'Southpaw', true, false, true, false, ARRAY['Wired, Wireless'], 'Gasket Mount', 'Aluminum', 'https://example.com/tofu65.jpg', true),
('Discipline65', 115.00, 'CFTKB', ARRAY['CFTKB'], ARRAY['100%'], ARRAY['ANSI'], 'Normal', false, false, false, false, ARRAY['Wired'], 'Plate Mount', 'Metal', 'https://example.com/discipline65.jpg', false),
('Keychron Q5 Pro', 270.00, 'Keychron', ARRAY['Keychron'], ARRAY['Split'], ARRAY['Ortholinear'], 'Alice', true, false, true, true, ARRAY['2.4Ghz, Wireless'], 'Tray Mount', 'Plastic', 'https://example.com/keychron-95.jpg', true);

-- Populate the 'lubricants' table
INSERT INTO public."lubricants" (name, price, img_url, availability) VALUES
('Krytox 205g0', 12.00, 'https://example.com/krytox-205g0.jpg', true),
('Tribosys 3203', 10.50, 'https://example.com/tribosys-3203.jpg', true),
('Super Lube', 7.99, 'https://example.com/super-lube.jpg', false);

-- Populate the 'builds' table
INSERT INTO public."builds" (build_name, kit_choice, switch_choice, keycap_choice, lubricant_choice) VALUES
('Minimalist Build', 'Tofu65', 'Gateron Yellow', 'ePBT Kuro/Shiro', 'Krytox 205g0'),
('Tactile Dream', 'Ergodox EZ', 'Holy Panda', 'MT3 Susuwatari', 'Tribosys 3203'),
('Clicky Classic', 'Discipline65', 'Kailh Box Jade', 'GMK Olivia', 'Super Lube');