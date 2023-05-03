# mester
Mester 

Functionality: 
- Create Account (simple member or worker "mester")
- Authentication
- Profile
- Filter
- Post
- Leave review
- Pay(optional*)
- Chatbox(optional*)


Members can:
- View list of workers "mesteri" (filter) and details 
- Add/post a job
- Leave review for a worker
- text with workers via chatbox(optional*)
- get notification via email when a workers accept his posts
Workers:
- get email notification when a job is posted in their field
- can view list of jobs
- can accept a job
- have calendar with available date
- can pay for a premium account so their name will always be in top of the list even if he has a low rating
- if worker get 1 star rating will not have permission to get another job for a number of days(not working with premium account)

Non Members:
-can only view the list of workers but not the details


Tabels:
- Members
- Workers (FK to Category)
- Category
- Jobs (FK to Members and FK to Category)
- Reviews (FK to Members and FK to Workers)

