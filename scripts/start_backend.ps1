$env:DATABASE_URL = "postgresql://paybridge:i9BGFpP17dXCASApnPoqJIYuiPc24pNs@dpg-dbqv46rbc2fs73f97hh0-a.oregon-postgres.render.com/paybridge_mosz?sslmode=require"
$env:SESSION_SECRET = "e353cbae68b2a33f352945a96e0f6764cf9ebb6830c6a13196d5cb50b81daafc"
$env:ENCRYPTION_KEY = "402112b37d4870667197ca0699f98089fa90dc1f4a14672f0ddc16aa2e7ad88c"
$env:PAYPAL_ENV = "sandbox"
$env:PAYPAL_API_BASE = "https://api-m.sandbox.paypal.com"
$env:APP_ENV = "development"
$env:ALLOW_DEV_AUTH = "true"
$env:PAYPAL_CLIENT_ID = "sandbox_paybridge_client_id_demo"
$env:PAYPAL_CLIENT_SECRET = "sandbox_paybridge_client_secret_demo"
$env:PORT = "8080"

cd services/api
go run ./cmd/api
