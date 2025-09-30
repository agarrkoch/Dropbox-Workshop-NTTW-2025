# Dropbox-Workshop-NTTW-2025

This is a quick guide for how to set up your dropbox account for API access, as well as a summar of the files in this repository. 

## Setting Up

To access the API you need to create an immutable “refresh token,” which will be used to create short-living “access tokens.”  These access tokens are used in the header to authorize all API calls. 

<ins>Step 1.</ins>

Create an account if you don’t have one already.

Regardless of your account type, you will have access to the dropbox API. Dropbox doesn’t publish rate limits, i.e. the number of HTTP requests you can make in a period of time, but they are very generous and you’re unlikely to exceed them. If you do, you should consider more efficient call patterns. As you gain experience, refer to this performance guide: https://developers.dropbox.com/dbx-performance-guide 

For a list of all HTTP endpoints, refer to this document: https://www.dropbox.com/developers/documentation/http/documentation
  
Steps 2 through 10 are a concise and accessible summary of the Authorization and /oauth2/authorize sections which make up the top part of this document

<ins>Step 2.</ins>

Create an application. To do so, click the following link and click “Create App” https://www.dropbox.com/developers/apps. 

<ins>Step 3.</ins>

For the purposes of this test application, design an app with the widest scope and access. Click “Create App” to continue. 

<img width="801" height="342" alt="image" src="https://github.com/user-attachments/assets/8f8e718c-9b2b-49a7-ae05-6c7d0571fb82" />

<ins>Step 4.</ins>

You will be redirected to your new applications settings page. Click the permissions tab.

<img width="348" height="84" alt="image" src="https://github.com/user-attachments/assets/5d7b7fbf-cf26-413b-8b56-6e1c9078438f" />

And set the widest Individual Scopes for the purposes of this test application, i.e. write permissions for all categories, and press submit. As you go on to create other applications, you can be more selective with permissions and explore the Team Scopes area. 

<img width="573" height="444" alt="image" src="https://github.com/user-attachments/assets/88588c1e-2d36-454a-b5c7-d278a303cb61" />

<ins>Step 5.</ins>

Return to the permission table and make a note of your App Key and your App Secret:

<img width="276" height="76" alt="image" src="https://github.com/user-attachments/assets/31b87c85-a57a-4964-8628-e5491bdd47df" />

<ins>Step 6.</ins>

Go to the following URL, but replace APPKEYHERE with your App Key. 

```
https://www.dropbox.com/oauth2/authorize?client_id=APPKEYHERE&response_type=code&token_access_type=offline
```

<ins>Step 7.</ins>

<ins>Step 8.</ins>

<ins>Step 9.</ins>

<ins>Step 10.</ins>
