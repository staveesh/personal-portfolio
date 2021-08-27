from flask import Flask, render_template, url_for

app = Flask(__name__)

user = {
    'page': '',
    'name': 'Taveesh Sharma',
    'shortname': 'Taveesh',
    'description': "Hi, my name is Taveesh Sharma. I am a researcher in the area of internet measurements and privacy.",
    "social": {
        'twitter': 'https://twitter.com/staveesh',
        'linkedin': 'https://www.linkedin.com/in/taveesh-sharma-9385a8197',
        'github': 'https://github.com/staveesh',
        'instagram': 'https://instagram.com/_taveesh',
        'facebook': 'https://www.facebook.com/taveeshsharma',
        'email': 'mailto:staveesh08@gmail.com'
    },
    'quote': "I figured I should have a website, because that's what everybody was doing ;-) ",
    'journey': {
        'jobs': [
            {
                'image': 'static/images/uctlogo.png',
                'designation': 'Research Assistant',
                'organization': 'University of Cape Town',
                'location': 'Cape Town, South Africa',
                'from': 'July 2021',
                'to': 'Present',
                'description': "Currently working on a research project known as 'Cost-aware security decision model'. The aim of this project is to enable users confgure their internet security on their own with the help of standard protocols. In addition, information related to cost of the chosen security settings will also be provided.",
                'tags': ['Networks', 'Security', 'Machine Learning', 'Internet measurements', 'Android']
            },
            {
                'image': 'static/images/epaylater.jpg',
                'designation': 'Software Development Engineer',
                'organization': 'ePayLater',
                'location': 'Gurgaon, India',
                'from': 'February 2020',
                'to': 'July 2020',
                'description': "ePayLater business helps in growing small businesses by allowing their owners to pay later for their purchases. Seller Dashboard is a product by ePayLater which allows small business owners to keep a track of their purchases, invoices and inventory from large distributors like Metro Cash & Carry. This solution integrates with ePayLater's payment gateway which allows the business owners to either pay upfront or pay using their credit limit (a maximum of INR 25,00,000). My role as a backend engineer on the Seller Dashboard was to introduce features like catalog upload, inventory management, order billing, order refunds and order analytics. Add-ons like an ElasticSearch backed search engine was also implemented for providing seamless look-ups for a range of items in the inventory.",
                'tags': ['FinTech', 'Payments', 'eCommerce', 'Credit', 'ElasticSearch', 'Dropwizard']
            },
            {
                'image': 'static/images/paypal.png',
                'designation': 'Software Engineer',
                'organization': 'PayPal',
                'location': 'Chennai, India',
                'from': 'July 2018',
                'to': 'October 2019',
                'description': "As part of the Analytical Data Services team (Chennai, Tel Aviv and Shanghai), I was involved in the development of business-critical functionalities that helped analysts productionalize fraud detection models. I also contributed to the 'TTM' initiative which resulted in the automation of 275 days of manual work per year. I also took the ownership of key features for the 'RADD simulation' project through which analysts could estimate the impact of fraud detection models in future. I received PayPal's 'Bravo' recognition for showcasing creative thinking and collaboration skills in internal tool development and support. I participated in many center-wide hackathons and actively volunteered for 'PayPal Gives' activities. I was also fortunate to attend the GIDS (Great International Developer Summit) and present it's highlights to my division.",
                'tags': ['Payments', 'Data Engineering', 'Analytics', 'SQL', 'Full Stack Dev']
            }
        ],
        'education': [
            {
                'image': 'static/images/uctlogo.png',
                'degree': 'MSc Computer Science',
                'university': 'University of Cape Town',
                'location': 'Cape Town, South Africa',
                'from': 'July 2020',
                'to': 'Present',
                'description': "I am currently pursuing my masters degree in Computer Science from University of Cape Town, South Africa. The title of my research is 'Investigating Optimal Internet Data Collection in Low-Resource Networks'. "
            },
            {
                'image': 'static/images/bits.png',
                'degree': 'BE Computer Science',
                'university': 'BITS Pilani',
                'location': 'Goa, India',
                'from': 'August 2014',
                'to': 'August 2018',
                'description': "Undergraduate studies at BITS Pilani acquainted me with the vast and challenging field of Computer Science. Some of the key subjects in the coursework were Data Structures and Algorithms, Computer Networks, Linear Algebra, Machine Learning, Artificial Intelligence, Neural Networks and Fuzzy Logic and Software Development for Portable Devices. Apart from coursework, I enjoyed teaching C and UNIX programming to first year students when I was a Professional Assistant for the course Computer Programming. It was a different experience altogether as it helped me strengthen my knowledge and engage with the subject even more. In the final year of my undergraduate studies, I worked on a very interesting project in the fields of robotics and IoT. I developed a robot that allows a person to remotely track the health of an elderly person or a patient. This robot is capable of receiving locomotory signals from a remotely located android phone over the internet in real-time. It was a challenging project - involving a deep understanding of internet protocols for video calling, Android OS, and Arduino UNO. I taught myself the basics of Android Programming and Robotics along with the coursework and completed the project successfully. As a result of my efforts, this project was awarded the highest marks in the class. I also showcased this project in an exhibition organized by the college and thoroughly enjoyed discussing it with the attendees. This project boosted my confidence as a Computer Science student and motivated me even more towards realizing my purpose."
            }
        ]
    },
    'publications': [
        "Taveesh Sharma and Josiah Chavula. 2021. Investigating Measurement Scheduling Strategies in Low Resource Networks (Poster). In ACM SIGCAS Conference on Computing and Sustainable Societies (COMPASS) (COMPASS’21), June 28-July 2, 2021, Virtual Event, Australia. ACM, New York, NY, USA, 4 pages.",
    ]
}


@app.route("/")
def home():
    user['page'] = 'home'
    return render_template('index.html', user=user)


@app.route("/resume")
def about():
    user['page'] = 'resume'
    return render_template('cv.html', user=user)


@app.route("/blog")
def contact():
    user['page'] = 'blog'
    return render_template('blog.html', user=user)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
