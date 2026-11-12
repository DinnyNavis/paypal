const https = require('https');
const crypto = require('crypto');
const apiKey = process.env.RENDER_API_KEY || 'rnd_slWiW5tuQ4bBQJYZB5BixZHWGjjz';

function req(method, path, data) {
  return new Promise((resolve, reject) => {
    const r = https.request({
      hostname: 'api.render.com',
      path: '/v1' + path,
      method: method,
      headers: {
        'Authorization': 'Bearer ' + apiKey,
        'Content-Type': 'application/json',
        'Accept': 'application/json'
      }
    }, res => {
      let b = '';
      res.on('data', c => b += c);
      res.on('end', () => resolve({ status: res.statusCode, body: b ? JSON.parse(b) : {} }));
    });
    r.on('error', reject);
    if (data) r.write(JSON.stringify(data));
    r.end();
  });
}

async function run() {
  const backendId = 'srv-dbqv1fd9fdbs73dq9ljg';
  const frontendId = 'srv-dbqv17o8v5cc73e93b1g';

  // 1. Set backend env vars
  const sessionSecret = crypto.randomBytes(32).toString('hex');
  const encKey = crypto.randomBytes(32).toString('hex');

  const backendEnvVars = [
    { key: 'SESSION_SECRET', value: sessionSecret },
    { key: 'ENCRYPTION_KEY', value: encKey },
    { key: 'PAYPAL_ENV', value: 'sandbox' },
    { key: 'PAYPAL_API_BASE', value: 'https://api-m.sandbox.paypal.com' },
    { key: 'APP_ENV', value: 'production' },
    { key: 'ALLOW_DEV_AUTH', value: 'true' }
  ];

  const res1 = await req('PUT', `/services/${backendId}/env-vars`, backendEnvVars);
  console.log('Backend env-vars status:', res1.status);

  // 2. Set frontend env vars
  const frontendEnvVars = [
    { key: 'VITE_API_URL', value: 'https://paybridge-api-service.onrender.com' }
  ];
  const res2 = await req('PUT', `/services/${frontendId}/env-vars`, frontendEnvVars);
  console.log('Frontend env-vars status:', res2.status);

  // 3. Check deploy status
  const d1 = await req('GET', `/services/${frontendId}/deploys?limit=2`);
  if (d1.body && d1.body[0]) {
    console.log('Frontend latest deploy status:', d1.body[0].deploy.status);
  }

  const d2 = await req('GET', `/services/${backendId}/deploys?limit=2`);
  if (d2.body && d2.body[0]) {
    console.log('Backend latest deploy status:', d2.body[0].deploy.status);
  }
}

run().catch(console.error);
