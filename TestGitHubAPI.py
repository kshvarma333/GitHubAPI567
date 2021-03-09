import unittest

from GitHubAPI import git_hub_api

class TestGitHubAPI(unittest.TestCase):
    def testgithubapi(self):
        """ Testing GitHubAPI"""
        lis = git_hub_api("richkempinski")
        self.assertEqual(lis[0],'Repo: csp Number of commits: 2')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()


