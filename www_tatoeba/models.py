# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=240)
    class Meta:
        db_table = u'auth_group'

class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    group_id = models.IntegerField()
    permission_id = models.IntegerField()
    class Meta:
        db_table = u'auth_group_permissions'

class AuthMessage(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    message = models.TextField()
    class Meta:
        db_table = u'auth_message'

class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150)
    content_type_id = models.IntegerField()
    codename = models.CharField(unique=True, max_length=250)
    class Meta:
        db_table = u'auth_permission'

class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(unique=True, max_length=90)
    email = models.CharField(unique=True, max_length=225)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    is_superuser = models.IntegerField()
    last_login = models.DateTimeField()
    date_joined = models.DateTimeField()
    password = models.CharField(max_length=150)
    lang = models.CharField(max_length=12, blank=True)
    since = models.DateTimeField()
    last_time_active = models.IntegerField()
    level = models.IntegerField()
    send_notifications = models.IntegerField()
    name = models.CharField(max_length=765)
    birthday = models.DateTimeField()
    description = models.TextField()
    homepage = models.CharField(max_length=765)
    image = models.CharField(max_length=765)
    country_id = models.CharField(max_length=6)
    is_public = models.IntegerField()

    class Meta:
        db_table = u'users'

class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    group_id = models.IntegerField()
    class Meta:
        db_table = u'auth_user_groups'

class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    permission_id = models.IntegerField()
    class Meta:
        db_table = u'auth_user_user_permissions'

class Contributions(models.Model):
    #id = models.IntegerField(primary_key=True)
    sentence_id = models.IntegerField()
    sentence_lang = models.CharField(max_length=12, blank=True)
    translation_id = models.IntegerField(null=True, blank=True)
    translation_lang = models.CharField(max_length=12, blank=True)
    text = models.CharField(max_length=1500)
    action = models.CharField(max_length=18)
    user_id = models.IntegerField(null=True, blank=True)
    datetime = models.DateTimeField()
    ip = models.CharField(max_length=45, blank=True)
    type = models.CharField(max_length=24)
    class Meta:
        db_table = u'contributions'

class Countries(models.Model):
    id = models.CharField(max_length=6, primary_key=True)
    iso3 = models.CharField(max_length=9, blank=True)
    numcode = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=240)
    class Meta:
        db_table = u'countries'

class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=300)
    app_label = models.CharField(unique=True, max_length=254)
    model = models.CharField(unique=True, max_length=254)
    class Meta:
        db_table = u'django_content_type'

class DjangoSession(models.Model):
    session_key = models.CharField(max_length=120, primary_key=True)
    session_data = models.TextField()
    expire_date = models.DateTimeField()
    class Meta:
        db_table = u'django_session'

class DjangoSite(models.Model):
    id = models.IntegerField(primary_key=True)
    domain = models.CharField(max_length=300)
    name = models.CharField(max_length=150)
    class Meta:
        db_table = u'django_site'

class FavoritesUsers(models.Model):
    favorite_id = models.IntegerField(unique=True)
    user_id = models.IntegerField(unique=True)
    class Meta:
        db_table = u'favorites_users'

class FollowersUsers(models.Model):
    follower_id = models.IntegerField(unique=True)
    user_id = models.IntegerField(unique=True)
    class Meta:
        db_table = u'followers_users'

class Groups(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=300)
    created = models.DateTimeField(null=True, blank=True)
    modified = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'groups'

class Langstats(models.Model):
    lang = models.CharField(max_length=12, blank=True)
    numberofsentences = models.IntegerField(db_column='numberOfSentences') # Field name made lowercase.
    class Meta:
        db_table = u'langStats'

class PrivateMessages(models.Model):
    id = models.IntegerField(primary_key=True)
    recpt = models.IntegerField()
    sender = models.IntegerField()
    user_id = models.IntegerField()
    date = models.DateTimeField()
    folder = models.CharField(max_length=15)
    title = models.CharField(max_length=765)
    content = models.TextField()
    isnonread = models.IntegerField()
    class Meta:
        db_table = u'private_messages'

class SentenceAnnotations(models.Model):
    id = models.IntegerField(primary_key=True)
    sentence_id = models.IntegerField()
    meaning_id = models.IntegerField()
    dico_id = models.IntegerField()
    text = models.CharField(max_length=2000)
    class Meta:
        db_table = u'sentence_annotations'

class SentenceComments(models.Model):
    id = models.IntegerField(primary_key=True)
    sentence_id = models.IntegerField()
    lang = models.CharField(max_length=12, blank=True)
    text = models.TextField()
    user_id = models.IntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'sentence_comments'

class Sentences(models.Model):
    id = models.IntegerField(primary_key=True)
    lang = models.CharField(max_length=12, blank=True)
    text = models.CharField(max_length=1500)
    correctness = models.IntegerField(null=True, blank=True)
    user_id = models.IntegerField(null=True, blank=True)
    created = models.DateTimeField(null=True, blank=True)
    modified = models.DateTimeField(null=True, blank=True)
    dico_id = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'sentences'

class SentencesLists(models.Model):
    id = models.IntegerField(primary_key=True)
    is_public = models.IntegerField()
    name = models.CharField(max_length=450)
    user_id = models.IntegerField(null=True, blank=True)
    numberofsentences = models.IntegerField(db_column='numberOfSentences') # Field name made lowercase.
    created = models.DateTimeField(null=True, blank=True)
    modified = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'sentences_lists'

class SentencesSentencesLists(models.Model):
    sentences_list_id = models.IntegerField(unique=True)
    sentence_id = models.IntegerField(unique=True)
    class Meta:
        db_table = u'sentences_sentences_lists'

class SentencesTranslations(models.Model):
    sentence_id = models.IntegerField()
    translation_id = models.IntegerField()
    sentence_lang = models.CharField(max_length=12, blank=True)
    translation_lang = models.CharField(max_length=12, blank=True)
    distance = models.IntegerField()
    class Meta:
        db_table = u'sentences_translations'

class SinogramSubglyphs(models.Model):
    sinogram_id = models.IntegerField()
    glyph = models.CharField(max_length=6, blank=True)
    subglyph = models.CharField(max_length=6)
    class Meta:
        db_table = u'sinogram_subglyphs'

class Sinograms(models.Model):
    id = models.IntegerField(primary_key=True)
    utf = models.CharField(max_length=24)
    glyph = models.CharField(max_length=30)
    strokes = models.IntegerField(null=True, blank=True)
    english = models.TextField(blank=True)
    chin_trad = models.CharField(max_length=30, db_column='chin-trad', blank=True) # Field renamed to remove dashes. Field name made lowercase.
    chin_simpl = models.CharField(max_length=30, db_column='chin-simpl', blank=True) # Field renamed to remove dashes. Field name made lowercase.
    chin_pinyin = models.CharField(max_length=765, db_column='chin-pinyin', blank=True) # Field renamed to remove dashes. Field name made lowercase.
    jap_on = models.CharField(max_length=765, db_column='jap-on', blank=True) # Field renamed to remove dashes. Field name made lowercase.
    jap_kun = models.CharField(max_length=765, db_column='jap-kun', blank=True) # Field renamed to remove dashes. Field name made lowercase.
    frequency = models.FloatField()
    checked = models.IntegerField()
    subcharacterslist = models.CharField(max_length=765, blank=True)
    usedbylist = models.CharField(max_length=765, db_column='usedByList', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'sinograms'

class Users(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(unique=True, max_length=60)
    password = models.CharField(max_length=150)
    email = models.CharField(unique=True, max_length=255)
    lang = models.CharField(max_length=12, blank=True)
    since = models.DateTimeField()
    last_time_active = models.IntegerField()
    level = models.IntegerField()
    group_id = models.IntegerField()
    send_notifications = models.IntegerField()
    name = models.CharField(max_length=765)
    birthday = models.DateTimeField()
    description = models.TextField()
    homepage = models.CharField(max_length=765)
    image = models.CharField(max_length=765)
    country_id = models.CharField(max_length=6)
    is_public = models.IntegerField()
    class Meta:
        db_table = u'users'

class Visitors(models.Model):
    ip = models.CharField(unique=True, max_length=45)
    timestamp = models.IntegerField()
    class Meta:
        db_table = u'visitors'

class Wall(models.Model):
    id = models.IntegerField(primary_key=True)
    owner = models.IntegerField()
    parent_id = models.IntegerField(null=True, blank=True)
    date = models.DateTimeField()
    title = models.CharField(max_length=765)
    content = models.TextField()
    lft = models.IntegerField(null=True, blank=True)
    rght = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'wall'

class WallThreadsLastMessage(models.Model):
    id = models.IntegerField(primary_key=True)
    last_message_date = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'wall_threads_last_message'

