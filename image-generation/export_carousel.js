const puppeteer = require('puppeteer');
const path = require('path');
const fs = require('fs');

async function exportCarousel() {
  const htmlPath = path.resolve(__dirname, 'carousel.html');
  
  if (!fs.existsSync(htmlPath)) {
    console.error('Error: carousel.html not found in current directory.');
    process.exit(1);
  }

  console.log('Launching browser to capture slides...');
  const browser = await puppeteer.launch({ headless: 'new' });
  const page = await browser.newPage();
  
  // Set viewport to ensure high resolution and correct layout
  await page.setViewport({ width: 1200, height: 8000, deviceScaleFactor: 2 });
  
  // Navigate to local file
  const fileUrl = `file://${htmlPath}`;
  await page.goto(fileUrl, { waitUntil: 'networkidle0' });

  // Get all slide elements
  const slides = await page.$$('.slide');
  
  if (slides.length === 0) {
    console.error('No elements with class "slide" found in carousel.html');
    await browser.close();
    process.exit(1);
  }

  console.log(`Found ${slides.length} slides. Exporting...`);

  // Capture each slide exactly
  for (let i = 0; i < slides.length; i++) {
    const slide = slides[i];
    const outputPath = path.resolve(__dirname, `slide_${i + 1}.png`);
    
    await slide.screenshot({
      path: outputPath,
      type: 'png'
    });
    console.log(`- Saved ${outputPath}`);
  }

  await browser.close();
  console.log('✅ Export complete!');
}

exportCarousel().catch(err => {
  console.error('Failed to export carousel:', err);
  process.exit(1);
});
