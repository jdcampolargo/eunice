import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        animal = request.form["animal"]
        response = openai.Completion.create(
            engine="text-davinci-001",
            prompt=generate_prompt(animal),
            temperature=0.6,
            max_tokens=64,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

    # if request.method == "POST":
    #     retry = request.form[animal]
    #     response = openai.Completion.create(
    #         engine="text-davinci-001",
    #         prompt=generate_prompt(retry),
    #         temperature=0.6,
    #         max_tokens=64,
    #         top_p=1,
    #         frequency_penalty=0,
    #         presence_penalty=0
    #     )




        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


    #once you get result, if box is empty, then another click (button could change --> (to keep going) 
    # and it would generating

    

    # for chat feature
    # create another def for chat like feature

    

    # response = openai.Completion.create(
        # engine="text-davinci-001",
        # prompt="ML Tutor: I am a ML/AI language model tutor\nYou: What is a language model?\nML Tutor: A language model is a statistical model that describes the probability of a word given the previous words.\nYou: What is a statistical model?",
        # temperature=0.3,
        # max_tokens=60,
        # top_p=1.0,
        # frequency_penalty=0.5,
        # presence_penalty=0.0,
        # stop=["You:"]
    # )

def generate_prompt(animal):
    return """Write an essay/report on 

Prompt: Two stages of a person's life
Answer: There are two stages of a person's life: the first stage is when they are young and carefree, and the second stage is when they are older and more responsible. The first stage of a person's life is when they are young and carefree. This is the time when they are just starting to learn about the world and figure out who they are. They are exploring new things and having fun. They are not yet responsible for their own actions, and they rely on their parents or guardians to take care of them. The second stage of a person's life is when they are older and more responsible. This is the time when they are working and taking care of their own needs. They may have a family and be responsible for their children. They are no longer exploring new things, but instead are focused on their responsibilities.
Prompt: Lab report on Measuring Actual Capacitance
Answer: Measuring Actual Capacitance Lab Group PI- Preston Bae - pjbae2 Analyst- Kannan Ramasawmy - kannanr2 Skeptic - Juan David Campolargo - jcampo37 Introduction In this lab, we’re interested in investigating how to measure the actual capacitance by measuring the actual capacitance of the 22µF capacitors. Experimentally, we determine the actual capacitance of the 22µF capacitors. We also determined the uncertainty on the measurement and compared it to the expected value of the capacitance. To do this experiment, we used four (4) wires, a breadboard, and a 10kΩ resistor. Methods First, connect the wires to the breadboard in a way that they are in parallel with one another. Second, connect the wire to the negative side of the battery. Third, connect the wire to the positive side of the battery. Fourth, connect the wire to the other end of the 10kΩ resistor. Finally, connect the wire that is connected to the 10kΩ resistor to the negative side of the battery. After that, measure the voltage on the + side of the resistor and the + side of the capacitor over time. You then use the equation V(t)=VOe-t/τ The iOLab gives V(t), VO, and we know what R is. Τ = RC. Once you get V(t) and VO from the iOLab, you just plug the numbers in and solve for C. After you solve for C, you should get the actual capacitance of the capacitor. Use this equation for the uncertainty of capacitance: Where: U = uncertainty, σ = standard deviation = range / 2 x̅ = sample mean = (τ1 + τ2 + τn) / n n = sample size = number of samples = 2 μ = (μ̅) = expected value. The standard deviation is the amount an x deviates from the mean. The standard deviation is calculated by following the steps below: First, find the sample mean. The sample mean is the average that is calculated by adding all of the x-values and then dividing the sum by the sample size. Second, find the sample size. The sample size is the number of values that were added together to find the average. Third, find the deviation. The deviation is the distance between the sample mean and the x-values. Example: 4 – 1.5 + 3 – 0.4 + 4 – 0.7 = 1.2 n = N/2 = 3/2 = 1.5 σ = √[(1.5)(1.5)(1.5)(1.5)] = 1.5 If the √[(1.5)(1.5)(1.5)(1.5)] = 1.5, then the √[(1.5)(1.5)(1.5)(1.5)] = 1.5. Results Repository capacitor 1 link. https://iolabrepository.azurewebsites.net/DatasetView/3d72f03fa956aff32bbb9c115fdd23ebdb0428a73024253e9da34331d7de43e8/863226c2-2775-431a-bdfb-b47c24f77935/293901/ Repository capacitor 2 link. https://iolabrepository.azurewebsites.net/DatasetView/3bf4d10d293b1b02a45c7f07f2889566a6e3aa2ee6589a57e60ca26cea2d7d3d/863226c2-2775-431a-bdfb-b47c24f77935/293917/ Capacitor #1 #2 iOLab Voltage 1.80 V 1.80 V0 1.790 V 1.791 V V(t) .298 V .128 V time 0.42 seconds .6 seconds τ .2344 .2274 Actual Capacitance 23.4E-6 F 22.27E-6 F V(t)=VOe-t/τ τ=RC Uncertainty for capacitance: σ= range/ 2 = (.2344-.2274)/2 = .0035 x̅ = sample mean = (τ1 + τ2 + τn) / n = 0.2309 n = sample size = number of samples = 2 δ= standard error = σ/sqrt(n) = .0035/sqrt(2) = 0.0024748 δC1 =C1 *sqrt(.0025 + (.0024748/τ1)^2) = 2.673 * 10^-6 δC2 =C2 * sqrt(.0025 + (.0024748/τ2)^2) = 2.57 * 10^-6 Final capacitance values in form result 土 uncertainty C1 = 23.4E-6 F 土 2.673 * 10^-6 C2 = 22.27E-6 F土2.57 * 10^-6 Discussion We observed a couple of interesting effects from the results. The actual capacitance of the 22µF is higher than the theoretical capacitance (22µF). This value of the capacitance is higher than the theoretical value due to the resistive capacitance. Also, our reliability is higher than the uncertainty. This is because we use a breadboard and we wrap the wires around the breadboard. This way, we can make more accurate measurements. The capacitance of the capacitors is slightly higher than 22µF. This is because of the variances of the dielectric constant of the resin, the amount of the resin, the size of the aluminum plates, and the size of the gap between the aluminum plates. All the measurements are done at room temperature, so the temperature should not affect the results. The measured capacitances are very accurate, but not exact. There still may be errors due to the resistance of the test equipment, the circuit board, the test current, the capacitance tolerance of the 22µF capacitors, etc. The actual capacitance of the 22µF 
Prompt: On today’s talk shows, guests and audience members often argue heatedly with each other, and on more than one occasion, guests and audience members have been hurt. Do today’s talk shows go too far? Explain your answer.
Answer: There is no easy answer to this question, as it depends on individual opinions. Some people may feel that talk shows today have gone too far in terms of inciting arguments and violence, while others may feel that this is simply a reflection of the current state of society and that talk shows are no different from other forms of entertainment. Ultimately, it is up to each individual to decide whether or not they believe that talk shows have gone too far.
Prompt: {}
Answer:""".format(
        animal.capitalize()
    )
