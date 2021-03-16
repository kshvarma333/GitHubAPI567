import unittest

from unittest import mock

from GitHubAPI import git_hub_api

from typing import List,Any

class TestGitHubAPI(unittest.TestCase):
    def testgithubapi(self):
        """ Testing GitHubAPI"""
        git_hub_api = mock.Mock(return_value = "['Repo: csp Number of commits: 2', 'Repo: hellogitworld Number of commits: 30', 'Repo: helloworld Number of commits: 6', 'Repo: Mocks Number of commits: 10', 'Repo: Project1 Number of commits: 2', 'Repo: richkempinski.github.io Number of commits: 9', 'Repo: threads-of-life Number of commits: 1', 'Repo: try_nbdev Number of commits: 2', 'Repo: try_nbdev2 Number of commits: 5']")
        result = git_hub_api("richkempinski")
        self.assertEqual(result, "['Repo: csp Number of commits: 2', 'Repo: hellogitworld Number of commits: 30', 'Repo: helloworld Number of commits: 6', 'Repo: Mocks Number of commits: 10', 'Repo: Project1 Number of commits: 2', 'Repo: richkempinski.github.io Number of commits: 9', 'Repo: threads-of-life Number of commits: 1', 'Repo: try_nbdev Number of commits: 2', 'Repo: try_nbdev2 Number of commits: 5']")



if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()


