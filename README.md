# Dropbox-Workshop-NTTW-2025

This is a quick guide for how to set up your dropbox account for API access, and a collection of the most relevant HTTP requests for archivists who are coding novices.

## Setting Up

To access the API you need to create an immutable “refresh token,” which will be used to create short-living “access tokens.”  These access tokens are used in the header to authorize all API calls. 

<ins>Step 1.</ins>

Create an account if you don’t have one already.

Regardless of your account type, you will have access to the dropbox API. Dropbox doesn’t publish rate limits, i.e. the number of HTTP requests you can make in a period of time, but they are very generous and you’re unlikely to exceed them. If you do, you should consider more efficient call patterns. As you gain experience, refer to this performance guide: https://developers.dropbox.com/dbx-performance-guide 

For a list of all HTTP endpoints, refer to this document: https://www.dropbox.com/developers/documentation/http/documentation
  
Steps 2 through 10 are a concise and accessible summary of the Authorization and /oauth2/authorize sections which make up the top part of the previously linked document

<ins>Step 2.</ins>

Create an application. To do so, click the following link and click “Create App” https://www.dropbox.com/developers/apps. 

<ins>Step 3.</ins>

For the purposes of this test application, design an app with the widest scope and access. Click “Create App” to continue. 

<ins>Step 4.</ins>

You will be redirected to your new applications settings page. Click the permissions tab.

And set the widest Individual Scopes for the purposes of this test application, i.e. write permissions for all categories, and press submit. As you go on to create other applications, you can be more selective with permissions and explore the Team Scopes area. 

<ins>Step 5.</ins>

Return to the permission table and make a note of your App Key and your App Secret:

<ins>Step 6.</ins>

Go to the following URL, but replace APPKEYHERE with your App Key. 

```
https://www.dropbox.com/oauth2/authorize?client_id=APPKEYHERE&response_type=code&token_access_type=offline
```

<ins>Step 7.</ins>

Press continue, then allow, and then make note of your access code.

<ins>Step 8.</ins>

You can now use the access code, app key, and app secret to create a request to retrieve your immutable refresh token.

We will run this simple HTTP request using bash in terminal. Subsequent HTTP requests will be made using Python, because that is my preferred coding language. 

Replace capitalized text with your values, and remove brackets.

For PC: Command prompt (NOT PowerShell)
```
curl -X POST https://api.dropbox.com/oauth2/token ^
    -d code=<AUTHORIZATION_CODE> ^
    -d grant_type=authorization_code ^
    -d client_id=<APP_KEY> ^
    -d client_secret=<APP_SECRET>
```
For Mac: Terminal
```
curl https://api.dropbox.com/oauth2/token \     
    -d code=<AUTHORIZATION_CODE> \     
    -d grant_type=authorization_code \     
    -d client_id=<APP_KEY> \
    -d client_secret=<APP_SECRET>
```

Common errors:
- The authorization code, app key, and appsecret are case sensitive. The authorization code also starts with a hyphen. Make sure all values are entered exactly as they were presented to you. 
- The authorization expired. Return to step six. 

<ins>Step 9.</ins>

Your output will look something like this. Make note of the value following “refresh token.” 

```
{
  "access_token": "sl.u.AGDTMF0mAuwD8reK17hYd1cnlmHSqR8K2WFefrEyaz96FfVMm5DpfK4W77zKsxBV1tGzcc1a0prklqhqymn4KWbouBK-J4BHL4T7nXyCT7l6ehjKFyBoNTAqnN3JNkYccUVubg1tG-4Park8WVqrb3_2P_6uD_YZJAVvGWWi4NWP-0pqA8nkKp_QWSFAXAm7K_8cYI0mufn0Ny8FX5ODtPdUQ8BGwEO4dYYpWqK7st64jnVLH1mLuuOnDNtmCC65hVtDgxYOQr4eGfvKGCFWTeNVg9B8wjYamdQxochwlDmfk765gaLacrF4kQfN53WpAyOpw-OYN_X9n85POQ_rrmZrTR1uIkajbfGn9N0-EaqvaWNEJsKDHTE6kaPSrzYH7b-f9gPsLiruvTsI-nPHrCSfMYpWUyFIo55rRbnem6kdkxOTOm666XKpYlLRiG3pcLkOqFL709NlO3fvTGwWA9JlrFFmqSSkB2nUmEnHyaBFp0VXL9cTdIbjoUP0M-fGuNFpYy2zbE3pvqn5r1eZ9vGIHpkJ85O5sCS2ITa9Ql_ME-8uamkfjRahneMRBtaDofBYBLnM43K7qv1vfygaFBVzN4V-gZJCnYPSRcz6RRO0r5uvwj_w36Xo3VmobvWmba44_I2vEMa8WxIINj4fmSl285O3syUY6lcXChvTrGOuJxD4aNvmUg8QD2lPIpEhnFLMqNmjgmS_nL3zGtePjlRWWsXtceQlOH5jSZNWiFlBaQSVh6_hCnJrEkfzSh2Q1C0U1vaCuRetn4GwCbD6k8lS0H1OQLr-bo-SThBOuMKRo57X6F6-BOPv7wVS0yObEp1SJ6f0uNAQEjrhMYsAvNvNx7EcKSVNmidbpad4NvkmhnhCeDIWFNtg2EJ32nET1pWcU-IMbS5jYhZ2cctaeRFQiStCbqifxohHsTMHYZvQAagw59fOZ4ComkQFlZIzmDH1GnII-eKauWddJs9v-YfqDabAObUz1juD68gm4Z-vCAtrXwZh-uxnYFl_bJ610B96gRon2xUwHbXMLf5FjkRGcG9AzT1UaJdTN_fZbU06_df2gDVIqAWQla8aaU1-4ir-dUDvx64iCnkPB6sa1FUV66bC7L7MVSeRyRSUTH7j1pw_A3J_F9uw42Cgsc1VYUGR7z7engXIn71QUoj4N9HTtnFPhWU5Hx4FrmH8qGuCosGHMeRPzsjd-ZxrjI5PT9LaoeUw4uYSUYZuO9baWgTCN_F0MlkF2LZCiLa5K3uM-8Pz79XNMuX5gvwPkgYS4u4aLIQILP6hnnMbxjundXewnbkLW6z7Jr8EwXewbID5cg",
  "token_type": "bearer",
  "expires_in": 14400,
  "refresh_token": "rlbMz0WYbAoAAAAAAAAAARyM3DMKiS4Z70Dom3B_VsI4KtApC0pA2NMPSHGa75Am",
  "scope": "account_info.read account_info.write contacts.read contacts.write file_requests.read file_requests.write files.content.write files.metadata.read files.metadata.write sharing.read sharing.write",
  "uid": "342658846",
  "account_id": "dbid:AAC64yFYM7rf7k0wkEyO0GKCI805vHmyYzk"
}
```

You’ll also notice that the output includes the access token and keys relevant to it. The access token is what is included in all API requests. These tokens are short-lived, and expire after a period of time. The “expires_in” value is in terms of seconds. If your Dropbox script needs a long time to run, keep in mind that you need to “refresh” this access token during the runtime of your script. 

<ins>Step 10.</ins>

Going forward, to get the access token from the refresh token, you will run this request:

```
curl https://api.dropbox.com/oauth2/token \
    -d grant_type=refresh_token \
    -d refresh_token=<REFRESH_TOKEN> \
    -d client_id=<APP_KEY> \
    -d client_secret=<APP_SECRET>
```
