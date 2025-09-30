# Dropbox-Workshop-NTTW-2025

This is a quick guide for how to set up your dropbox account for API access, as well as a summar of the files in this repository. 

## Setting Up

To access the API you need to create an immutable “refresh token,” which will be used to create short-living “access tokens.”  These access tokens are used in the header to authorize all API calls. 

1. Create an account if you don’t have one already.

  Regardless of your account type, you will have access to the dropbox API. Dropbox doesn’t publish rate limits, i.e. the number of HTTP requests you can make in a period of time, but they are very generous and you’re unlikely to exceed them. If you do, you should consider more efficient call patterns. As you gain experience, refer to this performance guide: https://developers.dropbox.com/dbx-performance-guide 
  
  For a list of all HTTP endpoints, refer to this document: https://www.dropbox.com/developers/documentation/http/documentation
  
  Steps 2 through 10 are a concise and accessible summary of the Authorization and /oauth2/authorize sections which make up the top part of this document


2. 
