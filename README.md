# Task appearance (simplified)
Task: to mark the vertices of the polyline from one end of the shape to the other
![QuCaptcha simplified appearance](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeYAg7wwDzCs9tNKEcyRsYmyArFIuzUKWAgPZUtctT_MvbARcER15DYcGdFos5T_J-8fEo1e7g31P_zEypctWgQGvR3odjTLGt94OAeUvPeqXmqcELjSBysQl7HSnQQFGD4NR8Xfg?key=dnTGlPGafZ97PkobWORP-axG)
# License
This project is licensed under the Apache License 2.0.
Contact: quartyom@gmail.com

# Requirements
```Python 3.6+
Flask
OpenCV (cv2)
```

# Client-side Integration (HTML/JS)
Add the following script to your HTML form. Replace {{ captcha_url }} with the actual URL of the CAPTCHA service:

```python
<form action="#" method="POST">
  <script class="qu-captcha-form qu-captcha-uses-cookie" src="{{ captcha_url }}/get_api" async></script>
  <button class="qu-captcha-disable-item" type="submit">Submit</button>
</form>
```

## Align CAPTCHA to the left:
```python
<div style="width:min-content;margin-left:0;">
  <script class="qu-captcha-form" src="{{ captcha_url }}/get_api" async></script>
</div>
```

# Available CSS Classes
```
qu-captcha-hide-item: hides elements until CAPTCHA is solved (via display: none)
qu-captcha-show-item: shows elements only after CAPTCHA is solved
qu-captcha-disable-item: disables elements until CAPTCHA is solved (disabled: true)
```
# Tracking CAPTCHA Completion in JavaScript
```JavaScript
const captchaResponse = document.getElementById('qu-captcha-human-token');
const observer = new MutationObserver((mutations) => {
  mutations.forEach((mutation) => {
    if (mutation.type === 'attributes' && mutation.attributeName === 'value') {
      console.log(captchaResponse.value);
    }
  });
});
observer.observe(captchaResponse, { attributes: true });
```

# Server-side Processing (Flask)
Example POST request handler in Flask:
```python
@app.route('/', methods=['POST'])
def handle_form():
    human_token = request.form.get('qu-captcha-human-token')
    verify_response = requests.post(
        f'{captcha_url}/validate_captcha',
        json={"api_token": captcha_api_token, "human_token": human_token}
    )
    result = verify_response.json()
    if result.get("valid", False) and result.get("ip", "") == request.remote_addr:
        return "CAPTCHA passed. User is human."
    return "CAPTCHA verification failed."
```
