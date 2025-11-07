{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/jaswanth34586/machine-learning-practice-questions/blob/main/experiment%207.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Experiment 7\n",
        "\n",
        "!pip install hmmlearn\n",
        "\n",
        "import numpy as np\n",
        "from hmmlearn import hmm\n",
        "\n",
        "# Create sample sequential data\n",
        "sequence = np.array([[0],[1],[2],[1],[0],[1],[2],[2],[1],[0]])\n",
        "model = hmm.MultinomialHMM(n_components=2, random_state=0)\n",
        "\n",
        "model.fit(sequence)\n",
        "\n",
        "logprob, predicted_states = model.decode(sequence, algorithm=\"viterbi\")\n",
        "print(\"Predicted hidden states:\", predicted_states)\n",
        "\n"
      ],
      "metadata": {
        "id": "_5Rqv9KhN2lc",
        "outputId": "20bcd4fe-401a-4e79-943f-f049724cd973",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: hmmlearn in /usr/local/lib/python3.12/dist-packages (0.3.3)\n",
            "Requirement already satisfied: numpy>=1.10 in /usr/local/lib/python3.12/dist-packages (from hmmlearn) (2.0.2)\n",
            "Requirement already satisfied: scikit-learn!=0.22.0,>=0.16 in /usr/local/lib/python3.12/dist-packages (from hmmlearn) (1.6.1)\n",
            "Requirement already satisfied: scipy>=0.19 in /usr/local/lib/python3.12/dist-packages (from hmmlearn) (1.16.3)\n",
            "Requirement already satisfied: joblib>=1.2.0 in /usr/local/lib/python3.12/dist-packages (from scikit-learn!=0.22.0,>=0.16->hmmlearn) (1.5.2)\n",
            "Requirement already satisfied: threadpoolctl>=3.1.0 in /usr/local/lib/python3.12/dist-packages (from scikit-learn!=0.22.0,>=0.16->hmmlearn) (3.6.0)\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "WARNING:hmmlearn.hmm:MultinomialHMM has undergone major changes. The previous version was implementing a CategoricalHMM (a special case of MultinomialHMM). This new implementation follows the standard definition for a Multinomial distribution (e.g. as in https://en.wikipedia.org/wiki/Multinomial_distribution). See these issues for details:\n",
            "https://github.com/hmmlearn/hmmlearn/issues/335\n",
            "https://github.com/hmmlearn/hmmlearn/issues/340\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Predicted hidden states: [1 0 1 0 1 0 1 0 1 0]\n"
          ]
        }
      ]
    }
  ],
  "metadata": {
    "colab": {
      "name": "Welcome To Colab",
      "provenance": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}