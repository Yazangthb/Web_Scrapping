from vertexai.language_models import ChatModel, InputOutputTextPair
import google.generativeai as palm

# Set the API key
palm.configure(api_key='AIzaSyDGEuFTUwVDuZeiEFqtj-Xl4nbzOf1cqYU')
# chat_model = ChatModel.from_pretrained("chat-bison-001")
# parameters = {
#     "temperature": 0,  # Temperature controls the degree of randomness in token selection.
#     "max_output_tokens": 256,  # Token limit determines the maximum amount of text output.
#     "top_p": 0.95,
#     # Tokens are selected from most probable to least until the sum of their probabilities equals the top_p value.
#     "top_k": 40,  # A top_k of 1 means the selected token is the most probable among all tokens.
# }
#
# chat = chat_model.start_chat(
#     context="My name is Miles. You are an astronomer, knowledgeable about the solar system.",
#     examples=[
#         InputOutputTextPair(
#             input_text="How many moons does Mars have?",
#             output_text="The planet Mars has two moons, Phobos and Deimos.",
#         ),
#     ],
# )
# response = chat.send_message(
#     "How many planets are there in the solar system?",**parameters
# )
# print(f"Response from Model: {response.text}")
# Choose a model
model = 'models/text-bison-001'



# Write your prompt
prompt = ("""Given the text which represents a scrapped website by the span components \
 identify the what is the purpose of the website\
text : {""Taqa Space is a brand of "TAQA SPACE LTD" Registered in England and Wales No: "14473829" Copyright © 2023 Taqa Space LTD - UK Resources:Privacy PolicyTerms and ConditionsRefund PolicyCancellation PolicyCookie Policy Always on, always creating - our team works 24/7 Born in the UK, but residing in the metaverse!\t\t\t\t About Us Courses TaqaTube Certificate Verification Contact Us About Us Courses TaqaTube Certificate Verification Contact Us Tel: +44 (0) 20 80400414 info@taqaspace.com Search Login Register Born in the UK, but residing in the metaverse! Toggle navigation About Us Courses TaqaTube Certificate Verification Contact Us Taqa Space > Courses Sort By: Release date (newest first) Release date (oldest first) Price high Price low Overall Rating Popular (most viewed) Filters Category Photovoltaic Business & Skills Subcategory Status Featured Hot New Special Level Beginner Intermediate Advanced Rating 4.5 & up 4.0 & up 3.5 & up 3.0 & up Instructors Hamzi Smadi Ala\'a Mannoun Rashed Albarakeh Sandro Abdel Hafith Eng. Laith Basha, Eng. Haitham Shaqra, Eng. Azzah AlKhalaileh, Eng. Faris Foudeh Show more Price Free Courses Paid Courses Only Subscription Reset all Certified Solar Structure Designer CSSD $650 taqaspace 10 Lectures 30 hours Preview this course Add to Wishlist Solar Standard Implementation Professional SSIP $450 15 Hours Certified Green Hydrogen Professional CGHP $950 ... 12 Lectures How I saved more than 8000$ using CANVA 5 $75 (2) 5 Lectures 2 Hours PV Hybrid Micro-Grids Professional PHMP $850 $399 (3) ... 11 Lectures 30 Hours Solar O&M Professional SOMP $750 $350 The SOMP Program\xa0is a comprehensive course that covers the principles and practices of operation and maintenance (O&M) for solar power systems.... The Smart PV Training SPVT $125 (1) 6 Hours Solar Structure Drawing Using AutoCad $45 ... Solar Career Planning Free (4) ... 8 Lectures Introduction to On-Grid PV System (6) ... 1 Hour Sketchup & Rendering for PV Projects SRPV Learn how to use Sketchup software in 3D drawing for solar PV systems and to do the shading analysis. Also, you will learn how to use Skelion tool ... 13 Lectures Certified PV System Professional CPVSP $249 (18) الخطوة الأولى لدخول عالم الأنظمة الكهروضوئية المرتبطة على الشبكة, يتميز هذا البرنامج بتركيزه\xa0على الجانب العملي والإبتعاد عن الجوانب النظرية الغير م... Load more Taqa Space LTD  Taqa Space is a brand of "TAQA SPACE LTD" Registered in England and Wales No: "14473829" Copyright © 2023 Taqa Space LTD - UK ContactsTel: +44 (0) 20 80400414info@taqaspace.comSocial Network Resources:Privacy PolicyTerms and ConditionsRefund PolicyCancellation PolicyCookie Policy Contacts  Tel: +44 (0) 20 80400414  info@taqaspace.com Social Network Login                 (https://taqaspace.com/user-account/) Register (https://taqaspace.com/user-account/) (https://taqaspace.com/) About Us (https://taqaspace.com/about-us/) Courses (https://taqaspace.com/courses/) TaqaTube (https://taqaspace.com/taqatube) Certificate Verification (https://taqaspace.com/cer) Contact Us (https://taqaspace.com/contact-us/) (https://taqaspace.com/user-account/)  (https://www.facebook.com/taqaspace)  (https://www.twitter.com/taqaspace)  (https://www.linkedin.com/company/taqaspace)  (https://www.instagram.com/taqaspace)  (https://t.me/+q6CVRkdBzThiODBk) About Us (https://taqaspace.com/about-us/) Courses (https://taqaspace.com/courses/) TaqaTube (https://taqaspace.com/taqatube) Certificate Verification (https://taqaspace.com/cer) Contact Us (https://taqaspace.com/contact-us/) Taqa Space (https://taqaspace.com) Filters\t (#) (https://taqaspace.com/courses/) (https://taqaspace.com/courses/cssd/) Preview this course\t\t (https://taqaspace.com/courses/cssd/) (https://taqaspace.com/user-account/) (https://taqaspace.com/courses/ssip/) Preview this course\t\t (https://taqaspace.com/courses/ssip/) (https://taqaspace.com/courses/cghp/) Preview this course\t\t (https://taqaspace.com/courses/cghp/) (https://taqaspace.com/courses/canva/) Preview this course\t\t (https://taqaspace.com/courses/canva/) (https://taqaspace.com/courses/phmp/) Preview this course\t\t (https://taqaspace.com/courses/phmp/) (https://taqaspace.com/courses/somp/) Preview this course\t\t (https://taqaspace.com/courses/somp/) (https://taqaspace.com/courses/spvt/) Preview this course\t\t (https://taqaspace.com/courses/spvt/) (https://taqaspace.com/courses/ssda/) Preview this course\t\t (https://taqaspace.com/courses/ssda/) (https://taqaspace.com/courses/scp/) Preview this course\t\t (https://taqaspace.com/courses/scp/) (https://taqaspace.com/courses/ios/) Preview this course\t\t (https://taqaspace.com/courses/ios/) (https://taqaspace.com/courses/srpv/) Preview this course\t\t (https://taqaspace.com/courses/srpv/) (https://taqaspace.com/courses/cpvsp/) Preview this course\t\t (https://taqaspace.com/courses/cpvsp/) (#) info@taqaspace.com (mailto:info@taqaspace.com)  (https://www.facebook.com/taqaspace)  (https://www.facebook.com/taqaspace)  (https://www.twitter.com/taqaspace)  (https://www.twitter.com/taqaspace)  (https://www.instagram.com/taqaspace)  (https://www.instagram.com/taqaspace)  (https://t.me/+q6CVRkdBzThiODBk)  (https://t.me/+q6CVRkdBzThiODBk) Privacy Policy (https://taqaspace.com/privacy/) Terms and Conditions (https://taqaspace.com/terms-and-conditions/)  (https://taqaspace.com/cancellation-policy/) Refund Policy (https://taqaspace.com/Refund-Policy/) Cancellation Policy (https://taqaspace.com/cancellation-policy/) Cookie Policy (https://taqaspace.com/cookie-policy/)""} """)

# Generate the response
completion = palm.generate_text(temperature=0.0,model=model, prompt=prompt)

# Print the response
print(completion.result)
