CREATE TABLE IF NOT EXISTS appointments (
  appointment_id VARCHAR(40) PRIMARY KEY,
  patient_id VARCHAR(40) NOT NULL,
  site VARCHAR(80) NOT NULL,
  specialty VARCHAR(120) NOT NULL,
  appointment_date VARCHAR(40) NOT NULL,
  created_at TIMESTAMP WITH TIME ZONE NOT NULL
);

