# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Time    : 2024/4/1 14:32
# @Author  : wangchongshi
# @Email   : wangchongshi.wcs@antgroup.com
# @FileName: test_rag_agent.py
import unittest

from agentuniverse.agent.agent import Agent
from agentuniverse.agent.agent_manager import AgentManager
from agentuniverse.agent.output_object import OutputObject
from agentuniverse.base.agentuniverse import AgentUniverse


class TranslationAgentTest(unittest.TestCase):
    """
    Test cases for the rag agent
    """

    def setUp(self) -> None:
        AgentUniverse().start(config_path='../../config/config.toml')

    def test_rag_fgent(self):
        data = """
        Last week, I spoke about AI and regulation at the U.S. Capitol at an event that was attended by legislative and business leaders. I’m encouraged by the progress the open source community has made fending off regulations that would have stifled innovation. But opponents of open source are continuing to shift their arguments, with the latest worries centering on open source's impact on national security. I hope we’ll all keep protecting open source!

Based on my conversations with legislators, I’m encouraged by the progress the U.S. federal government has made getting a realistic grasp of AI’s risks. To be clear, guardrails are needed. But they should be applied to AI applications, not to general-purpose AI technology.

Nonetheless, as I wrote previously, some companies are eager to limit open source, possibly to protect the value of massive investments they’ve made in proprietary models and to deter competitors. It has been fascinating to watch their arguments change over time.

For instance, about 12 months ago, the Center For AI Safety’s “Statement on AI Risk” warned that AI could cause human extinction and stoked fears of AI taking over. This alarmed leaders in Washington. But many people in AI pointed out that this dystopian science-fiction scenario has little basis in reality. About six months later, when I testified at the U.S. Senate’s AI Insight forum, legislators no longer worried much about an AI takeover.

Then the opponents of open source shifted gears. Their leading argument shifted to the risk of AI helping to create bioweapons. Soon afterward, OpenAI and RAND showed that current AI does not significantly increase the ability of malefactors to build bioweapons. This fear of AI-enabled bioweapons has diminished. To be sure, the possibility that bad actors could use bioweapons — with or without AI — remains a topic of great international concern.


The latest argument for blocking open source AI has shifted to national security. AI is useful for both economic competition and warfare, and open source opponents say the U.S. should make sure its adversaries don’t have access to the latest foundation models. While I don’t want authoritarian governments to use AI, particularly to wage unjust wars, the LLM cat is out of the bag, and authoritarian countries will fill the vacuum if democratic nations limit access. When, some day, a child somewhere asks an AI system questions about democracy, the role of a free press, or the function of an independent judiciary in preserving the rule of law, I would like the AI to reflect democratic values rather than favor authoritarian leaders’ goals over, say, human rights.

I came away from Washington optimistic about the progress we’ve made. A  year ago, legislators seemed to me to spend 80% of their time talking about guardrails for AI and 20% about investing in innovation. I was delighted that the ratio has flipped, and there was far more talk of investing in innovation.

Looking beyond the U.S. federal government, there are many jurisdictions globally. Unfortunately, arguments in favor of  regulations that would stifle AI development continue to proliferate. But I’ve learned from my trips to Washington and other nations’ capitals that talking to regulators does have an impact. If you get a chance to talk to a regulator at any level, I hope you’ll do what you can to help governments better understand AI.
        """
        """Test demo rag agent."""
        with open('/Users/weizj/jobspace/agentUniverse/sample_standard_app/app/test/test_file.txt') as f:
            data = f.read()
            print(len(data))

        instance: Agent = AgentManager().get_instance_obj('translation_by_token_agent')
        output_object: OutputObject = instance.run(source_lang="英文", target_lang="中文",
                                                   source_text=data
                                                   )
        res_info = f"\nRag agent execution result is :\n"
        res_info += output_object.get_data('output')
        # 创建文件，并写入文件
        with open('./rag_agent_result.txt', 'w') as f:
            f.write(res_info)
        print(res_info)


if __name__ == '__main__':
    unittest.main()
