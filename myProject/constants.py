from nltk.corpus import stopwords

NAME_PATTERN = [{'POS': 'PROPN'}, {'POS': 'PROPN'}]

# Education (Upper Case Mandatory)
EDUCATION = [
            'BE', 'B.E.', 'B.E', 'BS', 'B.S', 'ME', 'M.E', 'MCA', 'B.Sc', 'B.E (Computer Engineering)', 'BE (Computers)', 'Bachelor of Commerce (B.Com.)', 'Bachelor of Education (B.Ed.)', 'Bachelor of Arts (B.A.)', 'Graduation', 'Post Graduation', 'B.E. in Computer Science & Engineering', 'Master of Computer Applications (M.C.A)', 'Post Grad (MBA)', 'Bachelors of Engineering', 'BE(ENTC)', 'BE(Mechanical Engineering)', 'B.E.I.T', 'Diploma in teacher’s Education (D.T.Ed)', 'Masters of Arts', 'Bachelor of Arts', 'MBA in Material Management', 'B.com', 'Software Engineering', 'Post Graduate', 'M. Sc. in  IT',
            'M.E.', 'MS', 'M.S', 'BTECH', 'MTECH', 'B.tech', 'B.Tech', 'M.Tech', 'M.tech', 'B.sc in IT', 'BCS', 'MCS', 'DOEACC', 'Master of Business Administration', 'Bachelor of Science (B.Sc.)', 'MBA in Marketing', 'B.Sc. in Zoology and Chemistry', 'B. Tech in Electrical Engineering', ' D.E.E.E(Electrical & ElectronicsEngineering)', 'M.Tech. (IT)', 'PGDSM (Systems Management)', 'B.Tech/EEE', 'BCA (Bachelor of Computer Applications)', 'Master of Business Administration in marketing', ' Graduation in Computer Application', 'Masters in Business Administration(HR)', 'Bachelor in Computer Administration', 'Bachelor of Commerce','Diploma in Animation and Multimedia','B.A', 'BA', 'Bachelor of Arts', 'B.Tech in Computer Science & Engineering', 'PGDRM',
            'SSC', 'HSC', 'S.S.C', 'H.S.C', 'CBSE', 'ICSE', 'X', 'XII', 'Class X', 'Class XII', 'Diploma in Embedded Systems Design', 'Diploma in Computer Engineering', 'Diploma in Information Technology', 'Diploma in Electronics Engineering', 'B.E. (Electronics & Comm)', 'B.E. in Electronics and Telecommunication', 'B.E. in Electronics Engineering', 'PGDM (Finance)', 'B.E (Computer Engineering)', 'M.E. in Computer Engineering', 'B.E. in Computer Science', 'Diploma in Computer Science and Engineering', 'Post Graduate Diploma in Management', 'Bachelor of Business Administration', 'BBA', 'Bachelor’s Degree in Computer Science and Engineering', 'International MBA Program on Project Management', 'Bachelor of Computer Applications', 'BE in Information Technology', 'Post Graduate Certificate in Business Management', 'M.Tech. Computer Science', 'BE Information Technology', 'MBA (International Business)', 'BE (Computer Science)', 'MBA (Supply Chain Management)', 'B.Tech in Electrical & Electronics', 'B.TECH CSE', 'BE(Computer)',
        ]

NOT_ALPHA_NUMERIC = r'[^a-zA-Z\d]'

NUMBER = r'\d+'

# For finding date ranges
MONTHS_SHORT = r'''(jan)|(feb)|(mar)|(apr)|(may)|(jun)|(jul)
                   |(aug)|(sep)|(oct)|(nov)|(dec)'''
MONTHS_LONG = r'''(january)|(february)|(march)|(april)|(may)|(june)|(july)|
                   (august)|(september)|(october)|(november)|(december)'''
MONTH = r'(' + MONTHS_SHORT + r'|' + MONTHS_LONG + r')'
YEAR = r'(((20|19)(\d{2})))'

STOPWORDS = set(stopwords.words('english'))

RESUME_SECTIONS_PROFESSIONAL = [
                    'experience',
                    'education',
                    'interests',
                    'professional experience',
                    'publications',
                    'skills',
                    'certifications',
                    'objective',
                    'career objective',
                    'summary',
                    'leadership'
                ]

RESUME_SECTIONS_GRAD = [
                    'accomplishments',
                    'experience',
                    'education',
                    'interests',
                    'projects',
                    'professional experience',
                    'publications',
                    'skills',
                    'certifications',
                    'objective',
                    'career objective',
                    'summary',
                    'leadership'
                ]