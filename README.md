# site-for-finding-a-neighbor

## Installation

1. Clone the repository:

     ```bash
     git clone https://github.com/VL1507/site-for-finding-a-neighbor.git
     ```

2. Generate RSA keys:

     ```bash
     cd ./backend/app/
     mkdir certs
     openssl req -x509 -nodes -newkey rsa:2048 -keyout certs/jwt_private_key.pem -out certs/jwt_public_key.pem
     openssl req -x509 -nodes -newkey rsa:2048 -keyout certs/tgbot_jwt_private_key.pem -out certs/tgbot_jwt_public_key.pem
     ```
     copy tgbot_jwt_private_key.pem tgbot_jwt_public_key.pem in ./tg_bot/app/certs

3. Create a `.env` file. Use the `.env.example` as a reference.

4. Run the application:
