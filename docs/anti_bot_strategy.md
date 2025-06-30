# Anti-Bot Strategy for Job Scraping

## CAPTCHA Handling
- We avoid triggering CAPTCHA by:
  - Using randomized user-agents
  - Adding random delays (1.5s–3s)
  - Scraping during off-peak hours

## Proxy Strategy
- Rotating proxies from a list of open proxies
- Can be expanded using services like ScraperAPI or BrightData for production

## Session Handling
- Cookies and session headers preserved in Selenium sessions (for Indeed dynamic scraping)
