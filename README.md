# Exploring Psychometric Functions in a 3-Alternative Speech Classification Task

In this Jupyter notebook, we present a solution for an exercise proposed by Professor Tobias Andersen in the Cognitive Modeling course at DTU. The exercise revolves around discussing the utilities of the Psychometric Function in the context of a 3-alternative classification task.

## Experiment Overview

The classification task involves speech sounds categorized by an observer under varying sound intensities. The experiment comprises 30 trials for each sound intensity. The table below showcases the sound intensities (Is in dB) and the respective number of correct responses:

| Stimulus Intensity (Is in dB) | 5 | 10 | 15 | 20 | 25 | 30 |
|-------------------------------|---|----|----|----|----|----|
| Number of Correct Responses    | 12| 11 | 19 | 27 | 30 | 30 |

## Objective

Our objective is to fit three distinct psychometric functions based on Equations 1.19, 1.23, and 1.24 to the provided data. We will be making an assumption for the probability of guessing a correct response, denoted as Pguess, which is calculated as Pguess = 1/Nr, where Nr represents the number of response alternatives. Additionally, we treat the probability of lapsing, Plapse, as a free parameter in our model for a more accurate representation.

## Psycometric Functions Equations

![image](https://github.com/adrianlopezpirvu/DTU/assets/116965884/93468873-1817-408a-b63c-016ec2d1f6dd)

![image](https://github.com/adrianlopezpirvu/DTU/assets/116965884/35820d4e-fecf-4b37-9a9d-fe545543d756)

![image](https://github.com/adrianlopezpirvu/DTU/assets/116965884/21930dca-63c5-4326-a087-496b5d6838df)

Where:
- Φ: Gaussian cumulative distribution function.
- I: The stimulus intensity.
- c (Criterion): The "c" parameter in a psychometric function represents the criterion or bias                    of the decision maker. It determines the position along the stimulus axis at                    which the decision maker is equally likely to respond with one of the.
- σ: Standard deviation.
- Pguess: Probability of guessing correctly.
- Plapse: Lapsing is when an observer fails to perform the task perhaps due to a lapse in attention.

## Notebook explanation

In the first cell we import the libraries and functions we require for our code. 

Then we use a Jupyter cell for defining each Psycometric function. We define placeholders for parameters 'c' and 'σ' which will be optimized later (initial guess). We plot them individually and then together.

Later we define the Negative Log-likelihood, we can calculate it following next expression:
​![image](https://github.com/adrianlopezpirvu/DTU/assets/116965884/4aa53354-7c69-42dd-8f74-15ac6dcfd24b)

It is important to have clear that, we calculate the likelihood of each stimulus and because we supose they are i.i.d, we can calculate the total Likelihood by multiplying them. However, we use the log-Likelihood so it is the sum of the 6 points.

Now we move to the optimization part where we want to minimize, because it is the negative Likelihood. We use the minimize function from Sicpy.

We add some prints and plots to compare the results between the Psycometrics functions with initial guess values for the parameters and the optimized ones. We also compare the results of the 3 psycometric functions.

Also there are some coding and statisti explanations in the code.

## Greetings

Thank you very much to teacher Tobias Andersen for this inspiring exercice.


