const https = require('https');
const API_KEY = process.env.RENDER_API_KEY || 'rnd_slWiW5tuQ4bBQJYZB5BixZHWGjjz';
const deployId = process.argv[2] || 'dep-dbqvb93l550s73dti75g';
const serviceId = process.argv[3] || 'srv-dbqv1fd9fdbs73dq9ljg';

function req(path) {
  return new Promise((resolve, reject) => {
    const r = https.request({
      hostname: 'api.render.com',
      path: '/v1' + path,
      method: 'GET',
      headers: {
        'Authorization': 'Bearer ' + API_KEY,
        'Accept': 'application/json'
      }
    }, res => {
      let resData = '';
      res.on('data', c => resData += c);
      res.on('end', () => resolve(JSON.parse(resData)));
    });
    r.on('error', reject);
    r.end();
  });
}

function sleep(ms) { return new Promise(r => setTimeout(r, ms)); }

async function poll() {
  for (let i = 0; i < 40; i++) {
    const deploy = await req('/services/' + serviceId + '/deploys/' + deployId);
    const ts = new Date().toISOString().slice(11, 19);
    console.log('[' + ts + '] Deploy ' + deployId + ' status: ' + deploy.status);
    if (deploy.status === 'live' || deploy.status === 'build_failed' || deploy.status === 'update_failed' || deploy.status === 'canceled') {
      return deploy;
    }
    await sleep(6000);
  }
}

poll()
  .then(d => {
    console.log('Final Deploy Status: ' + (d ? d.status : 'timeout'));
    process.exit(d && d.status === 'live' ? 0 : 1);
  })
  .catch(err => {
    console.error(err);
    process.exit(1);
  });
