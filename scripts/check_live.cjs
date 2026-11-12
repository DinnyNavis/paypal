const https = require('https');
const API_KEY = process.env.RENDER_API_KEY || 'rnd_slWiW5tuQ4bBQJYZB5BixZHWGjjz';

function get(path) {
  return new Promise((resolve, reject) => {
    const req = https.request({
      hostname: 'api.render.com',
      path: '/v1' + path,
      method: 'GET',
      headers: {
        'Authorization': 'Bearer ' + API_KEY,
        'Accept': 'application/json'
      }
    }, res => {
      let data = '';
      res.on('data', chunk => data += chunk);
      res.on('end', () => {
        try {
          resolve(JSON.parse(data));
        } catch (e) {
          resolve(data);
        }
      });
    });
    req.on('error', reject);
    req.end();
  });
}

function checkUrl(url) {
  return new Promise((resolve) => {
    const req = https.get(url, (res) => {
      let data = '';
      res.on('data', c => data += c);
      res.on('end', () => resolve({ status: res.statusCode, body: data.slice(0, 100) }));
    });
    req.on('error', (err) => resolve({ error: err.message }));
  });
}

async function main() {
  const services = await get('/services?limit=10');
  console.log('--- RENDER SERVICES ---');
  for (const s of services) {
    const svc = s.service;
    console.log(`Service: ${svc.name} (${svc.id}) [${svc.type}]`);
    const url = svc.serviceDetails?.url;
    console.log(`  URL: ${url}`);
    const deploys = await get(`/services/${svc.id}/deploys?limit=1`);
    if (Array.isArray(deploys) && deploys[0]) {
      console.log(`  Deploy Status: ${deploys[0].deploy.status} (${deploys[0].deploy.id})`);
    }
  }

  // Also check databases
  const dbs = await get('/postgres?limit=10');
  console.log('--- POSTGRES DATABASES ---');
  if (Array.isArray(dbs)) {
    for (const d of dbs) {
      const db = d.postgres;
      console.log(`DB: ${db.name} (${db.id}) | Status: ${db.status} | Version: ${db.version}`);
    }
  }

  console.log('\n--- LIVE HTTP CHECKS ---');
  const feCheck = await checkUrl('https://paybridge-web-app.onrender.com');
  console.log('Frontend (paybridge-web-app):', feCheck);
  const beCheck = await checkUrl('https://paybridge-api-service.onrender.com/healthz');
  console.log('Backend /healthz (paybridge-api-service):', beCheck);
}

main().catch(console.error);
