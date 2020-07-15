# Generated by Django 2.2.12 on 2020-07-14 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("common", "0069_auto_20200703_1437")]

    operations = [
        migrations.AlterField(
            model_name="repository",
            name="algorithm",
            field=models.CharField(
                choices=[
                    (
                        "neural_network_internal",
                        "Neural Network with internal vocabulary",
                    ),
                    (
                        "neural_network_external",
                        "Neural Network with external vocabulary (BETA)",
                    ),
                    (
                        "transformer_network_diet",
                        "Transformer Neural Network with internal vocabulary",
                    ),
                    (
                        "transformer_network_diet_word_embedding",
                        "Transformer Neural Network with word embedding external vocabulary",
                    ),
                    (
                        "transformer_network_diet_bert",
                        "Transformer Neural Network with BERT word embedding",
                    ),
                ],
                default="transformer_network_diet",
                max_length=50,
                verbose_name="algorithm",
            ),
        ),
        migrations.AlterField(
            model_name="repositoryversionlanguage",
            name="algorithm",
            field=models.CharField(
                choices=[
                    (
                        "neural_network_internal",
                        "Neural Network with internal vocabulary",
                    ),
                    (
                        "neural_network_external",
                        "Neural Network with external vocabulary (BETA)",
                    ),
                    (
                        "transformer_network_diet",
                        "Transformer Neural Network with internal vocabulary",
                    ),
                    (
                        "transformer_network_diet_word_embedding",
                        "Transformer Neural Network with word embedding external vocabulary",
                    ),
                    (
                        "transformer_network_diet_bert",
                        "Transformer Neural Network with BERT word embedding",
                    ),
                ],
                default="transformer_network_diet",
                max_length=50,
                verbose_name="algorithm",
            ),
        ),
    ]
