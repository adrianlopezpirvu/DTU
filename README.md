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
Ψ (I) = P (r = yes | I) = Φ ((I − cI)/σI)                    (1.19)

Ψ (I) = (1 − Pguess) * Φ ((I − cI)/σI) + Pguess              (1.23)

Ψ (I) = (1 − Pguess − Plapse) * Φ ((I − cI)/σI) + Pguess     (1.24)

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

Later we define the Negative Log-likelihood; we can calculate it following next expression:
​![image](https://github.com/adrianlopezpirvu/DTU/assets/116965884/4aa53354-7c69-42dd-8f74-15ac6dcfd24b)






