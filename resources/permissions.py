def can_modify_resource(user, resource):
    return (
        user==resource.created_by or
        user.has_perm('resources.change_resource') 
        
    )

def can_delete_resource(user, resource):
    return (
        user==resource.created_by or
        user.has_perm('resources.delete_resource')  
    )