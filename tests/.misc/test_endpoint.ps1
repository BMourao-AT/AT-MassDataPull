$body = @{
    grant_type = "client_credentials"
    client_id = "6CxRFLmWerv-_Mrthl2ykbDz0mo"
    client_secret = "TA5lMz-trQKXFQiNdiYdXe9xtlkE-CEWfwgqffcSWUchWai0ke7LAA"
    scope = "monitoring"
}

$response = Invoke-RestMethod -Uri "https://app.ninjarmm.com/ws/oauth/token" `
    -Method POST `
    -ContentType "application/x-www-form-urlencoded" `
    -Body $body

$response | ConvertTo-Json