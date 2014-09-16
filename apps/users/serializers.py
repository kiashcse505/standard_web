# from django.contrib.auth.models import User, Group
# from rest_framework import serializers
# from apps.mpayment.serializers import PaymentMethodSerializer
# from apps.users.models import Profile, PaymentProfile, TransactionProfile, UserPaymentMethod


# class UserSerializer(serializers.ModelSerializer):

#     sex = serializers.RelatedField('sex')

#     class Meta:
#         model = User
#         fields = ('id','username', 'email', 'groups' )


# class GroupSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Group
#         fields = ('id','name',)


# class TransactionProfileSerializer(serializers.ModelSerializer):

#     transaction_type = serializers.SerializerMethodField('get_transaction_type')
#     status = serializers.SerializerMethodField('get_status')
#     entry_type = serializers.SerializerMethodField('get_entry_type')

#     def get_transaction_type(self,obj):
#         return obj.get_transaction_type_display()

#     def get_status(self,obj):
#         return obj.get_status_display()

#     def get_entry_type(self, obj):
#         return obj.get_entry_type_display()

#     class Meta:
#         model = TransactionProfile



# class UserPaymentMethodSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = UserPaymentMethod

# class ProfileSerializer(serializers.ModelSerializer):
#     user = UserSerializer()

#     class Meta:
#         model = Profile

# class PaymentProfileSerializer(serializers.ModelSerializer):

#     default_payment_method = PaymentMethodSerializer()

#     class Meta:
#         model = PaymentProfile
#         exclude = ('user', 'id' )


# from push_notifications.models import GCMDevice

# class GCMDSerializer(serializers.ModelSerializer):

#     def save_object(self, obj, **kwargs):
#         try:
#             GCMDevice.objects.get( user=obj.user, registration_id=obj.registration_id )
#         except:
#             super(GCMDSerializer, self).save_object(obj)
            
#     class Meta:
#         model = GCMDevice
#         fields = ( 'id', 'name','user','registration_id', )
