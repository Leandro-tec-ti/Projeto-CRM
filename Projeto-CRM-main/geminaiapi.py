import google.generativeai as genai

genai.configure(api_key="AIzaSyDg3H8ObRz-Ba8co8u_pC1NLhckkrC3oas")

model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("quantos anos o mundo tem?")
print(response.text)