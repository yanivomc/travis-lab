from travispy import TravisPy

t = TravisPy.github_auth('156d4e141465c32f02d5dd2a5cdac41811242cd1')
user = t.user()
repos = t.repos(member=user.login)

print ("User name logged:", user.login)

print len(repos)
print ("Project name ", repos[0].slug)

# Restart last build
repo = t.repo('yanivomc/travis-lab')
print ("The last build ID is: ", repo.last_build_id)
build = t.build(repo.last_build_id)
print build

print build.restart()


