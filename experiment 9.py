{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/jaswanth34586/machine-learning-practice-questions/blob/main/experiment%209.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Experiment 9\n",
        "\n",
        "from sklearn.datasets import load_iris\n",
        "from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier\n",
        "from sklearn.model_selection import train_test_split\n",
        "\n",
        "data = load_iris()\n",
        "X, y = data.data, data.target\n",
        "\n",
        "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)\n",
        "\n",
        "rf = RandomForestClassifier()\n",
        "rf.fit(X_train, y_train)\n",
        "\n",
        "ada = AdaBoostClassifier()\n",
        "ada.fit(X_train, y_train)\n",
        "\n",
        "print(\"Random Forest Accuracy:\", rf.score(X_test, y_test))\n",
        "print(\"AdaBoost Accuracy:\", ada.score(X_test, y_test))\n"
      ],
      "metadata": {
        "id": "xrlOq0JPOckf",
        "outputId": "e20a9ecb-eac2-400f-f016-dfa12def4855",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 14,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Random Forest Accuracy: 0.9555555555555556\n",
            "AdaBoost Accuracy: 0.9555555555555556\n"
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