curl --request POST \
  --url https://api.cohere.com/v1/embed-jobs/id/cancel \
  --header 'accept: application/json' \
  --header 'content-type: application/json' \
  --header "Authorization: bearer $CO_API_KEY"