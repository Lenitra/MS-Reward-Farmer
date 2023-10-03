// fonction async nom : tessss
async function tessss() {
    const browser = await puppeteer.launch({ headless: false }); // headless: false permet de voir la navigation dans le navigateur.
    const page = await browser.newPage();

    // Définissez le user agent pour simuler un navigateur mobile
    await page.setUserAgent('Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1');

    // Accédez à Bing
    await page.goto('https://www.bing.com/search?q=test');

    // await browser.close();
};