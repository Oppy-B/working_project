CREATE TABLE hotel(id serial, name text, address text, phone_num text, booking_dates daterange NOT NULL,
    EXCLUDE USING spgist (booking_dates WITH &&)
);