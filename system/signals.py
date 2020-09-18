from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.models import Group


from .models import customer


#signal chai user create garda customer pani banau ko lagi ho
def customer_profile(sender, instance, created, **kwargs):
	if created:
        # user register bhayepaxi kun group ma halni bhanna ko lagi-->admin or customer banaune
		group = Group.objects.get(name='customer')
		instance.groups.add(group)
		customer.objects.create(
			user=instance,
			name=instance.username,
			)
		print('Profile created!')

post_save.connect(customer_profile, sender=User)
