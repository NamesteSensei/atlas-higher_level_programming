-- Create the 'states' table
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

-- Insert sample data into the 'states' table
INSERT INTO states (name) VALUES ('California'), ('Arizona'), ('Texas');
