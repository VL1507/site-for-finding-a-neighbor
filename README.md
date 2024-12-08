# backend

## Installation

1. Clone the repository:

     ```bash
     git clone https://github.com/
     ```

2. Generate RSA keys:

     ```bash
     mkdir certs
     openssl genrsa -out certs/jwt-private.pem 2048
     openssl rsa -in certs/jwt-private.pem -pubout -out certs/jwt-public.pem
     ```

3. Create a `.env` file. Use the `.env.example` as a reference.

4. Run the application:
