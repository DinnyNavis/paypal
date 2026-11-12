const https = require('https');
const API_KEY = process.env.RENDER_API_KEY || 'rnd_slWiW5tuQ4bBQJYZB5BixZHWGjjz';
const SERVICE_ID = 'srv-dbqv1fd9fdbs73dq9ljg';

function req(method, path, body) {
  return new Promise((resolve, reject) => {
    const data = body ? JSON.stringify(body) : null;
    const r = https.request({
      hostname: 'api.render.com',
      path: '/v1' + path,
      method: method,
      headers: {
        'Authorization': 'Bearer ' + API_KEY,
        'Content-Type': 'application/json',
        'Accept': 'application/json'
      }
    }, res => {
      let resData = '';
      res.on('data', c => resData += c);
      res.on('end', () => {
        try { resolve(JSON.parse(resData)); }
        catch(e) { resolve(resData); }
      });
    });
    r.on('error', reject);
    if (data) r.write(data);
    r.end();
  });
}

async function configureAndDeploy() {
  console.log('1. Setting environment variables on backend...');
  const envVars = [
    { key: 'DATABASE_URL', value: 'postgresql://paybridge:i9BGFpP17dXCASApnPoqJIYuiPc24pNs@dpg-dbqv46rbc2fs73f97hh0-a/paybridge_mosz' },
    { key: 'SESSION_SECRET', value: 'e353cbae68b2a33f352945a96e0f6764cf9ebb6830c6a13196d5cb50b81daafc' },
    { key: 'ENCRYPTION_KEY', value: '402112b37d4870667197ca0699f98089fa90dc1f4a14672f0ddc16aa2e7ad88c' },
    { key: 'PAYPAL_ENV', value: 'sandbox' },
    { key: 'PAYPAL_API_BASE', value: 'https://api-m.sandbox.paypal.com' },
    { key: 'PAYPAL_CLIENT_ID', value: 'sandbox_paybridge_client_id_demo' },
    { key: 'PAYPAL_CLIENT_SECRET', value: 'sandbox_paybridge_client_secret_demo' },
    { key: 'APP_ENV', value: 'development' },
    { key: 'ALLOW_DEV_AUTH', value: 'true' }
  ];

  const envRes = await req('PUT', `/services/${SERVICE_ID}/env-vars`, envVars);
  console.log('Env vars updated:', envRes.length ? envRes.length + ' variables' : envRes);

  console.log('2. Updating service details (build & start command)...');
  const patchRes = await req('PATCH', `/services/${SERVICE_ID}`, {
    serviceDetails: {
      envSpecificDetails: {
        buildCommand: 'go build -o bin/api ./cmd/api',
        startCommand: './bin/api'
      },
      healthCheckPath: '/healthz'
    }
  });
  console.log('Service updated:', patchRes.id || patchRes);

  console.log('3. Triggering fresh deploy...');
  const deployRes = await req('POST', `/services/${SERVICE_ID}/deploys`, {
    clearCache: 'clear'
  });
  console.log('Deploy triggered:', deployRes.id, 'status:', deployRes.status);
  return deployRes.id;
}

configureAndDeploy()
  .then(deployId => {
    console.log('DEPLOY_ID=' + deployId);
  })
  .catch(console.error);
