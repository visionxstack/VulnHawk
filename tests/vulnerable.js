// tests/vulnerable.js
// Intentionally vulnerable JavaScript file for VulnHawk scanner testing.
// DO NOT use in production.

// [HIGH] Hardcoded Stripe API key
const stripeKey = "sk-test-4eC39HqLyjWDarjtT1zdp7dc";

// [HIGH] Hardcoded password
const password = "my_super_secret_password";

// [HIGH] Hardcoded API token
const API_TOKEN = "token_abc123XYZsecret99";

// [HIGH] innerHTML assignment — XSS risk
function updateUI(content) {
    document.getElementById('output').innerHTML = content;
}

// [MEDIUM] document.write usage
function renderPage(data) {
    document.write("Loading: " + data);
}

// [HIGH] eval() usage — arbitrary code execution
function runCommand(userInput) {
    eval(userInput);
}

// [MEDIUM] MD5 weak hashing — Node.js crypto
const crypto = require('crypto');
const hash = crypto.createHash('md5').update('sensitiveData').digest('hex');

// [MEDIUM] SHA1 weak hashing
const sha1hash = crypto.createHash('sha1').update('userData').digest('hex');
