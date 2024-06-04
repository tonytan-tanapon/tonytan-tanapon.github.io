def generate_email_info(subject, body, to_email, name, position):
    email_info = f"""
{to_email}
{subject}
{body}
"""
    filename = "email\\out\\"+to_email+".txt"
    with open(filename, 'w') as file:
        file.write(email_info.strip())
    
    print("Email information has been written to "+filename)

# Usage
subject = "Job Application: Data Science, AI Engineering, and Software Engineering Positions"
body = """
Dear Simon Davies,

My name is Tony Tantisripreecha, and I recently received my green card to work in the USA under the EB2-NIW category. I hold extensive experience as a Computer Science lecturer at Mahidol University in Thailand. I am currently seeking job opportunities in the fields of Data Science, AI Engineering, and Software Engineering.

With over a decade of experience in Mathematics and Computer Science, I have developed a strong skill set in Java, Python, C, C++, C#, SQL, and various other technologies. My professional background includes roles in academia and the financial technology sector, with a focus on software development, web development, AI, and machine learning.

I am particularly interested in opportunities where I can leverage my expertise and contribute to your organization. Please find my resume and professional links below for your reference:

Resume: https://tonytan-tanapon.github.io/TanaponResume.pdf
LinkedIn Profile: https://www.linkedin.com/in/tonytan-tanapon/
GitHub: https://github.com/tonytan-tanapon
Personal Website: https://tonytan-tanapon.github.io/

Thank you for considering my application. I look forward to the possibility of discussing how my skills and experiences align with your team\'s needs.

Best regards,

Tony Tantisripreecha
Email: tonytan.tanapon@gmail.com
Mobile: +1-202-498-4658
"""

import pandas as pd 
 
df = pd.read_csv("email\emaillist.csv",header=None)

for index, row in df.iterrows():
    email = row[0]
    name = row[1]
    position = row[2]
    
    generate_email_info(subject, body, email, name, position)
