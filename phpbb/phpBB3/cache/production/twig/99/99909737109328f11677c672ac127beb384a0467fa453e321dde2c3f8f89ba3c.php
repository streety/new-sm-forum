<?php

/* @phpbb_viglink/event/acp_help_phpbb_stats_before.html */
class __TwigTemplate_be2f9c0d5c72731d486c095ccbb1f16df3c17211402b79525f8cd7a396b2c78e extends Twig_Template
{
    public function __construct(Twig_Environment $env)
    {
        parent::__construct($env);

        $this->parent = false;

        $this->blocks = array(
        );
    }

    protected function doDisplay(array $context, array $blocks = array())
    {
        // line 1
        if (($context["S_VIGLINK_ASK_ADMIN"] ?? null)) {
            // line 2
            echo "\t<p>";
            echo $this->env->getExtension('phpbb\template\twig\extension')->lang("ACP_VIGLINK_SUPPORT_EXPLAIN");
            echo "</p>
";
        }
    }

    public function getTemplateName()
    {
        return "@phpbb_viglink/event/acp_help_phpbb_stats_before.html";
    }

    public function isTraitable()
    {
        return false;
    }

    public function getDebugInfo()
    {
        return array (  21 => 2,  19 => 1,);
    }

    /** @deprecated since 1.27 (to be removed in 2.0). Use getSourceContext() instead */
    public function getSource()
    {
        @trigger_error('The '.__METHOD__.' method is deprecated since version 1.27 and will be removed in 2.0. Use getSourceContext() instead.', E_USER_DEPRECATED);

        return $this->getSourceContext()->getCode();
    }

    public function getSourceContext()
    {
        return new Twig_Source("", "@phpbb_viglink/event/acp_help_phpbb_stats_before.html", "");
    }
}
