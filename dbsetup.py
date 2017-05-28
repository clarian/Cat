import shelve
Vitals = shelve.open("Catvitals")
Vitals['build'] = {'version':0.2}
Vitals['admins'] = []
Vitals['botdetails'] = {'prefix':'!','description':'bot created by Timmy.'}
Vitals.close()