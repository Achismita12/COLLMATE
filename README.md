# COLLMATE

Topic: AI BASED COLLECTION MANAGEMENT

A.	Project Title –
AI COLLMATE: AI based collection management

B.	 Business Objective: 
1.	Automated Debt Recovery Process
o	AI-driven automation helps streamline collection processes, reducing manual effort and increasing efficiency.
2.	Predictive Analytics for Risk Assessment
o	AI analyzes customer data to predict the likelihood of default and enables proactive engagement with borrowers.
3.	Optimized Recovery Strategies
o	Machine learning algorithms determine the best course of action for different customer segments, improving recovery rates.
4.	Enhanced Decision-Making
o	AI provides real-time insights and dashboards to help collection teams make data-driven decisions.
5.	Cost Reduction and Efficiency Gains
o	Automating collections reduces operational costs, allowing banks to allocate resources more effectively.

C.	Features to be used:
•	Monthly Income: Approximation of borrower’s income.
Here's a brief overview of each point:
1.	Collection Attempts: Refers to the number of times the creditor has reached out to collect overdue payments.
2.	Repayment Frequency: The schedule or interval (e.g., monthly, bi-weekly) at which loan payments are to be made.
3.	Last Payment Since: The date on which the most recent payment towards the loan was recorded.
4.	Rate of Interest: The percentage charged on the loan amount annually for borrowing funds.
5.	EMI (Equated Monthly Installment): The fixed monthly payment made to repay the loan, including both principal and interest.
6.	Type of Loan: Specifies the nature of the loan, such as car, home, education, or personal loan.
7.	Tenure of Loan: The total period during which the borrower is expected to repay the loan in full.
8.	Age: The borrower's age, which helps assess eligibility and repayment capacity.
9.	Occupation: The borrower's job or employment status, considered for evaluating income stability.
10.	Monthly SMA Type: SMA (Special Mention Account) categorizes overdue payments based on delay duration, helping track early signs of distress.
11.	Gender: The borrower's gender, which may sometimes be recorded for demographic analysis purposes.
12.	DPD (Days Past Due): The number of days a payment has been overdue from the scheduled repayment date.

D.	Data preprocessing steps needed

Database Integration
Feature: Connect to an Oracle database to fetch and manage customer data.
Database Table: CustomerAccounts.
  - Columns:
i.	Name
ii.	Account Number
iii.	Monthly Income
iv.	Collection Attempts
v.	Repayment Frequency
vi.	Last Payment since
vii.	Rate of Interest
viii.	EMI
ix.	Type of Loan (Car, Home…etc)]
x.	Tenure of Loan
xi.	Age
xii.	Occupations  
xiii.	Monthly SMA Type
xiv.	Gender
xv.	DPD

Rules and Constraints:
  Unique Account Numbers: Ensures no duplicate account numbers are generated.
  SMA Category Rules: SMA0=1-30 days
			SMA1=31-60days
			SMA2=61-90 days
  Calling/SMS/Visit Logic: These are made based on the SMA category and predefined frequencies.
SMA0=reminder through sms/call
SMA1=increase sms/call frequencies
SMA2=call/sms+visit

E.	Model Output
Synthetic Data Creation: We generate artificial financial data resembling real-world transactions to train and test the AI model effectively.
SMA Clustering: Categorizes overdue payments (SMA0, SMA1, SMA2) to prioritize efforts and determine outreach methods (SMS, call, or visit).
Age group Clustering: Clustering individuals by age and SMA characteristics helps uncover patterns and develop personalized treatment strategies. Enhances understanding across different age group.

GOAL  ::  The objective is to develop an AI-driven model for efficient collection management. This system will enable businesses to recover debts seamlessly, reducing costs while streamlining the entire process for greater ease and effectiveness.
