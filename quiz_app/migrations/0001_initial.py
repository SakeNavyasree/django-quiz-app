from django.db import migrations, models
import django.db.models.deletion


def set_default_option_a(apps, schema_editor):
    Question = apps.get_model('quiz_app', 'Question')
    for question in Question.objects.all():
        if not question.choice_a:
            question.choice_a = "default option"
            question.save()


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.TextField()),
                ('choice_a', models.CharField(max_length=255, default='default option')),  # Set default here
                ('choice_b', models.CharField(max_length=255)),
                ('choice_c', models.CharField(max_length=255)),
                ('choice_d', models.CharField(max_length=255)),
                ('correct_choice', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='QuizSession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_answer', models.CharField(max_length=1)),
                ('is_correct', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz_app.question')),
            ],
        ),
        # Add the migration to set default values for existing data
        migrations.RunPython(set_default_option_a),
    ]
