{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNLcdWPxe7x21PysKna8qYZ"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "source": [
        "!mkdir -p /content/jars\n",
        "!wget -O /content/jars/spark-cobol_2.12-2.11.0.jar https://repo1.maven.org/maven2/za/co/absa/cobrix/spark-cobol_2.12/2.11.0/spark-cobol_2.12-2.11.0.jar\n",
        "!wget -O /content/jars/cobol-parser_2.12-2.11.0.jar https://repo1.maven.org/maven2/za/co/absa/cobrix/cobol-parser_2.12/2.11.0/cobol-parser_2.12-2.11.0.jar"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "rffhyoJqVs9E",
        "outputId": "9207c858-7017-4ad6-d735-9f15d3502361"
      },
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "--2026-08-11 15:00:49--  https://repo1.maven.org/maven2/za/co/absa/cobrix/spark-cobol_2.12/2.11.0/spark-cobol_2.12-2.11.0.jar\n",
            "Resolving repo1.maven.org (repo1.maven.org)... 104.18.18.12, 104.18.19.12, 2606:4700::6812:130c, ...\n",
            "Connecting to repo1.maven.org (repo1.maven.org)|104.18.18.12|:443... connected.\n",
            "HTTP request sent, awaiting response... 200 OK\n",
            "Length: 352600 (344K) [application/java-archive]\n",
            "Saving to: ‘/content/jars/spark-cobol_2.12-2.11.0.jar’\n",
            "\n",
            "\r          /content/   0%[                    ]       0  --.-KB/s               \r/content/jars/spark 100%[===================>] 344.34K  --.-KB/s    in 0.03s   \n",
            "\n",
            "2026-08-11 15:00:49 (10.5 MB/s) - ‘/content/jars/spark-cobol_2.12-2.11.0.jar’ saved [352600/352600]\n",
            "\n",
            "--2026-08-11 15:00:49--  https://repo1.maven.org/maven2/za/co/absa/cobrix/cobol-parser_2.12/2.11.0/cobol-parser_2.12-2.11.0.jar\n",
            "Resolving repo1.maven.org (repo1.maven.org)... 104.18.18.12, 104.18.19.12, 2606:4700::6812:120c, ...\n",
            "Connecting to repo1.maven.org (repo1.maven.org)|104.18.18.12|:443... connected.\n",
            "HTTP request sent, awaiting response... 200 OK\n",
            "Length: 1937289 (1.8M) [application/java-archive]\n",
            "Saving to: ‘/content/jars/cobol-parser_2.12-2.11.0.jar’\n",
            "\n",
            "/content/jars/cobol 100%[===================>]   1.85M  --.-KB/s    in 0.07s   \n",
            "\n",
            "2026-08-11 15:00:49 (27.6 MB/s) - ‘/content/jars/cobol-parser_2.12-2.11.0.jar’ saved [1937289/1937289]\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [],
      "metadata": {
        "id": "Kn09oIalXvnE"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "!apt-get update\n",
        "!apt-get install -y openjdk-8-jdk-headless\n",
        "!pip install pyspark==3.4.0"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "OcyU50tYV02q",
        "outputId": "1ef75564-6d54-4ddd-c9ba-1288b0a751b5"
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\r0% [Working]\r            \rHit:1 http://archive.ubuntu.com/ubuntu jammy InRelease\n",
            "\r0% [Connecting to security.ubuntu.com (91.189.92.24)] [Connected to cloud.r-pro\r                                                                               \rHit:2 https://cli.github.com/packages stable InRelease\n",
            "\r0% [Waiting for headers] [Connecting to security.ubuntu.com (91.189.92.24)] [Wa\r                                                                               \rHit:3 http://archive.ubuntu.com/ubuntu jammy-updates InRelease\n",
            "\r0% [Connecting to security.ubuntu.com (91.189.92.24)] [Waiting for headers] [Co\r                                                                               \rHit:4 https://cloud.r-project.org/bin/linux/ubuntu jammy-cran40/ InRelease\n",
            "\r0% [Waiting for headers] [Connecting to security.ubuntu.com (91.189.92.24)] [Wa\r                                                                               \rHit:5 http://archive.ubuntu.com/ubuntu jammy-backports InRelease\n",
            "\r0% [Waiting for headers] [Waiting for headers] [Connected to ppa.launchpadconte\r0% [Waiting for headers] [Waiting for headers] [Connected to ppa.launchpadconte\r                                                                               \rHit:6 https://r2u.stat.illinois.edu/ubuntu jammy InRelease\n",
            "Hit:7 http://security.ubuntu.com/ubuntu jammy-security InRelease\n",
            "Hit:8 https://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu jammy InRelease\n",
            "Hit:9 https://ppa.launchpadcontent.net/ubuntugis/ppa/ubuntu jammy InRelease\n",
            "Reading package lists... Done\n",
            "W: Skipping acquire of configured file 'main/source/Sources' as repository 'https://r2u.stat.illinois.edu/ubuntu jammy InRelease' does not seem to provide it (sources.list entry misspelt?)\n",
            "Reading package lists... Done\n",
            "Building dependency tree... Done\n",
            "Reading state information... Done\n",
            "openjdk-8-jdk-headless is already the newest version (8u492-ga~us2-0ubuntu1~22.04.1).\n",
            "0 upgraded, 0 newly installed, 0 to remove and 137 not upgraded.\n",
            "Requirement already satisfied: pyspark==3.4.0 in /usr/local/lib/python3.12/dist-packages (3.4.0)\n",
            "Requirement already satisfied: py4j==0.10.9.7 in /usr/local/lib/python3.12/dist-packages (from pyspark==3.4.0) (0.10.9.7)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import os\n",
        "os.environ[\"JAVA_HOME\"] = \"/usr/lib/jvm/java-8-openjdk-amd64\"\n",
        "os.environ[\"PATH\"] = os.environ[\"JAVA_HOME\"] + \"/bin:\" + os.environ[\"PATH\"]"
      ],
      "metadata": {
        "id": "aG3tDAdfV67f"
      },
      "execution_count": 3,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from pyspark.sql import SparkSession\n",
        "\n",
        "spark = SparkSession.builder \\\n",
        "    .appName(\"CobolColabJarExample\") \\\n",
        "    .config(\"spark.jars\", \"/content/jars/spark-cobol_2.12-2.11.0.jar,/content/jars/cobol-parser_2.12-2.11.0.jar\") \\\n",
        "    .getOrCreate()"
      ],
      "metadata": {
        "id": "UmdOOKgSV-DQ"
      },
      "execution_count": 4,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df = spark.read.format(\"cobol\") \\\n",
        "    .option(\"copybook\", \"file:///content/test1_copybook.cob\") \\\n",
        "    .load(\"file:///content/example.bin\")\n",
        "\n",
        "df.printSchema()\n",
        "df.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "IgnhsECPWCtr",
        "outputId": "cfb42e64-1d13-4bef-f53f-43f1615939cb"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "root\n",
            " |-- ID: integer (nullable = true)\n",
            " |-- COMPANY: struct (nullable = true)\n",
            " |    |-- SHORT_NAME: string (nullable = true)\n",
            " |    |-- COMPANY_ID_NUM: integer (nullable = true)\n",
            " |    |-- COMPANY_ID_STR: string (nullable = true)\n",
            " |-- METADATA: struct (nullable = true)\n",
            " |    |-- CLIENTID: string (nullable = true)\n",
            " |    |-- REGISTRATION_NUM: string (nullable = true)\n",
            " |    |-- NUMBER_OF_ACCTS: integer (nullable = true)\n",
            " |    |-- ACCOUNT: struct (nullable = true)\n",
            " |    |    |-- ACCOUNT_DETAIL: array (nullable = true)\n",
            " |    |    |    |-- element: struct (containsNull = true)\n",
            " |    |    |    |    |-- ACCOUNT_NUMBER: string (nullable = true)\n",
            " |    |    |    |    |-- ACCOUNT_TYPE_N: integer (nullable = true)\n",
            " |    |    |    |    |-- ACCOUNT_TYPE_X: string (nullable = true)\n",
            "\n",
            "+---+-----------------+--------------------+\n",
            "| ID|          COMPANY|            METADATA|\n",
            "+---+-----------------+--------------------+\n",
            "|  1|{FOO INCORP, 0, }|{, , 1, {[{000000...|\n",
            "|  2|{BARCOMPANY, 0, }|{, , 1, {[{002000...|\n",
            "|  3|{EXAMPLE.CO, 0, }|{, , 1, {[{000000...|\n",
            "|  4|{EXAMPLE330, 0, }|{, , 2, {[{000000...|\n",
            "|  5|  {EXAMPLE3, 0, }|{, , 1, {[{000000...|\n",
            "|  6|  {EXAMPLE4, 0, }|{, , 3, {[{000000...|\n",
            "|  7|  {EXAMPLE7, 0, }|{, , 2, {[{000000...|\n",
            "|  8|   {FOOBAR8, 0, }|{, , 3, {[{000000...|\n",
            "|  9| {DUMMY_CO9, 0, }|{, , 1, {[{000000...|\n",
            "| 10|{NEWEXCOM10, 0, }|{, , 2, {[{000000...|\n",
            "+---+-----------------+--------------------+\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df = spark.read.format(\"cobol\") \\\n",
        "    .option(\"copybook\", \"file:///content/test1_copybook.cob\") \\\n",
        "    .load(\"file:///content/example.bin\")\n",
        "\n",
        "df.write.mode(\"overwrite\").json(\"file:///content/output_json\")"
      ],
      "metadata": {
        "id": "R4caZga0Wk-9"
      },
      "execution_count": 6,
      "outputs": []
    }
  ]
}