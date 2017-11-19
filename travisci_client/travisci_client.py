from travispy import TravisPy

t = TravisPy.github_auth('a8a470484a3876aa338e8fddfa3cfcdcfb037850')
user = t.user()
repos = t.repos(member=user.login)

print (" User name logged:", user.login)

print len(repos)
print ("Project name ", repos[0].slug)

# Restart last build
repo = t.repo('yanivomc/travis-lab')
print ("The last build ID is: ", repo.last_build_id)
build = t.build(repo.last_build_id)

