# Ignore SSL Warning
[Net.ServicePointManager]::ServerCertificateValidationCallback = { $true }

# Create Web Http request to URI
$uri = "https://google.com/" 
$webRequest = [Net.HttpWebRequest]::Create($uri)

# Get URL Information
$webRequest.ServicePoint

# Retrieve the Information for URI
$webRequest.GetResponse() | Out-NULL

# Get SSL Certificate and its details
$webRequest.ServicePoint.Certificate

# Get SSL Certificate Expiration Date
$webRequest.ServicePoint.Certificate.GetExpirationDateString()
